"""
Python-equivalent of ``avif_example_decode_file.c``.
"""

import os
import sys

from avif import AVIFError
from _avif import ffi, lib


def main():
    filename = os.fsencode(sys.argv[1])

    rgb = ffi.new("avifRGBImage*")
    decoder = lib.avifDecoderCreate()

    lib.avifDecoderSetIOFile(decoder, filename)  # TODO: nonexistent file
    result = lib.avifDecoderParse(decoder)  # TODO: failed decode
    if result != lib.AVIF_RESULT_OK:
        raise AVIFError.from_result(result)

    image = decoder.image
    print(f"Parsed AVIF: {image.width}x{image.height} ({image.depth}bpc)")

    while lib.avifDecoderNextImage(decoder) == lib.AVIF_RESULT_OK:
        lib.avifRGBImageSetDefaults(rgb, decoder.image)
        lib.avifRGBImageAllocatePixels(rgb)
        lib.avifImageYUVToRGB(decoder.image, rgb)

        first_pixel = tuple(rgb.pixels[0:4])
        print(f" * First pixel: RGBA{first_pixel}\n")


if __name__ == "__main__":
    main()
