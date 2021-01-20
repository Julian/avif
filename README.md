# `avif`

[![PyPI version](https://img.shields.io/pypi/v/avif.svg)](https://pypi.org/project/avif/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/avif.svg)](https://pypi.org/project/avif/)
[![Build status](https://github.com/Julian/avif/workflows/CI/badge.svg)](https://github.com/Julian/avif/actions?query=workflow%3ACI)

Python bindings for [libavif](https://github.com/AOMediaCodec/libavif) (via [CFFI](https://cffi.readthedocs.io/en/latest/))


## Installation

To install this module you will need to compile libavif yourself. If you want to make use of the decoder you will also need to also compile one (decoders/encoders can be compiled with libavif).

**List of available AV1 decoders:**

- **aom** (recommended)
- dav1d
- libgav1
- rav1e
- svt

If you compile avif without an AV1 decoder you will get `AVIFError: No codec available`  raised when you try to get a result, but you will still be able to import python module.

The installation steps shows how to compile libavif with aom decoder.



**Installation steps:**

- [Linux](INSTALL.linux.md)
- [Windows](INSTALL.win.md)




## Examples

Examples can be found under [examples](https://github.com/Julian/avif/tree/main/examples) directory.

You can use `sample.avif` if you don't have any avif encoded image for testing. Sample is 128x128 pixels in size and it's all white (RGBA: 255,255,255,255).

To test if library works properly run:

```bash
cd examples
python avif_example_decode_file.py sample.avif
```

Correct output:

```
Parsed AVIF: 128x128 (8bpc)
 * First pixel: RGBA(255, 255, 255, 255)
```

