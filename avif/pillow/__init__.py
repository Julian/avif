"""
Pillow plugin for decoding animated and static avif files. (only 8bit)
Based on:
https://github.com/python-pillow/Pillow/blob/master/src/PIL/WebPImagePlugin.py
"""

from io import BytesIO

from PIL import Image, ImageFile

from _avif import ffi, lib
from avif import Decoder


def _accept(data):

    possible_ftyp = (b"avif", b"avis", b"mif1")

    return data[4:8] == b"ftyp" and data[8:12] in possible_ftyp


class AvifImageFile(ImageFile.ImageFile):

    format = "AVIF"
    format_description = "Image container for AV1 video frames"

    _current_frame = -1
    _seek_to_frame = 0

    def _open(self):

        self._rgb_plane = ffi.new("avifRGBImage*")
        self._avif_decoder = Decoder()
        self.fc = self.fp.read()

        self.avif_image = self._avif_decoder.parse_data(self.fc)

        if self.avif_image.depth != 8:
            raise NotImplementedError("Image depth is not 8 bits.")

        self._size = (self.avif_image.width, self.avif_image.height)

        self.n_frames = self._avif_decoder._decoder.imageCount
        self.is_animated = self.n_frames > 1
        self.mode = "RGBA"  # only RGBA for now
        self.rawmode = self.mode
        self.tile = []

    def seek(self, n):

        self._seek_to_frame = n

    def _get_frame(self):

        self.avif_image = self._avif_decoder.nth_image(self._current_frame)

        lib.avifRGBImageSetDefaults(self._rgb_plane, self.avif_image)
        lib.avifRGBImageAllocatePixels(self._rgb_plane)
        lib.avifImageYUVToRGB(self.avif_image, self._rgb_plane)

        data = bytes(
            ffi.unpack(
                self._rgb_plane.pixels,
                self._size[0] * self._size[1] * 4,
            ),
        )

        return data

    def load(self):

        if self._current_frame != self._seek_to_frame:

            self._current_frame = self._seek_to_frame

            data = self._get_frame()

            if self.fp and self._exclusive_fp:
                self.fp.close()
            self.fp = BytesIO(data)

            self.tile = [("raw", (0, 0) + self.size, 0, self.rawmode)]

            return super().load()


Image.register_open(AvifImageFile.format, AvifImageFile, _accept)
Image.register_extension(AvifImageFile.format, ".avif")
Image.register_mime(AvifImageFile.format, "image/avif")
