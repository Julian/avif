"""
Python-equivalent of ``avif_example_decode_file.c``.
"""

import sys

from _avif import ffi, lib
from avif import Decoder


def main():
    filename = sys.argv[1]

    rgb = ffi.new("avifRGBImage*")
    decoder = Decoder()

    image = decoder.parse_path(filename)
    print(f"Parsed AVIF: {image.width}x{image.height} ({image.depth}bpc)")

    for image in decoder.next_images():
        lib.avifRGBImageSetDefaults(rgb, image)
        lib.avifRGBImageAllocatePixels(rgb)
        lib.avifImageYUVToRGB(image, rgb)

        pixels = rgb.pixels
        if rgb.depth > 8:
            pixels = ffi.cast("uint16_t *", pixels)

        first_pixel = tuple(pixels[0:4])
        print(f" * First pixel: RGBA{first_pixel}")


if __name__ == "__main__":
    main()
