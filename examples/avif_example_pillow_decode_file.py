"""
A Pillow-using example similar to ``avif_example_decode_file.py``.

Current limitation is Pillow not supporting 10 and 12 bit modes.
"""

import sys

from PIL import Image

# activates avif support in Pillow
import avif.pillow  # noqa: F401


def main():
    filename = sys.argv[1]

    image = Image.open(filename)

    print(f"Parsed AVIF: {image.width}x{image.height} (Mode: {image.mode})")

    if image.is_animated:
        print(f"Image is animated and has {image.n_frames} frames.")

    for i in range(image.n_frames):
        image.seek(i)

        first_pixel = image.getpixel((0, 0))

        print(f" * First pixel: RGBA{first_pixel}")


if __name__ == "__main__":
    main()
