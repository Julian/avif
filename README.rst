========
``avif``
========

|PyPI| |Pythons| |CI|

.. |PyPI| image:: https://img.shields.io/pypi/v/avif.svg
  :alt: PyPI version
  :target: https://pypi.org/project/avif/

.. |Pythons| image:: https://img.shields.io/pypi/pyversions/avif.svg
  :alt: Supported Python versions
  :target: https://pypi.org/project/avif/

.. |CI| image:: https://github.com/Julian/avif/workflows/CI/badge.svg
  :alt: Build status
  :target: https://github.com/Julian/avif/actions?query=workflow%3ACI


Python bindings for `libavif <https://github.com/AOMediaCodec/libavif>`_ (via
`CFFI <https://cffi.readthedocs.io/en/latest/>`_)


Installation
------------

To install this module you will need to compile libavif yourself. If you want to make use of the decoder you will also need to compile one (decoders/encoders can be compiled with libavif).


**List of available AV1 decoders:**

- **aom** (recommended)
- dav1d
- libgav1
- rav1e
- svt

If you compile avif without an AV1 decoder you will get ``AVIFError: No codec available`` raised when you try to get a result, but you will still be able to import python module.

The installation steps show how to compile libavif with aom decoder.


**Installation steps:**

- `Linux <INSTALL.linux.rst>`_
- `Windows <INSTALL.win.rst>`_


Examples
--------

Examples can be found under `examples <https://github.com/Julian/avif/tree/main/examples>`_ directory.

You can use ``sample.avif`` if you don't have any avif encoded image for testing.
Sample is 128x128 pixels in size and it's all white *(RGBA: 255, 255, 255, 255)*.

To test if library works properly run:

.. code-block:: bash

   cd examples
   python avif_example_decode_file.py sample.avif

Correct output::

   Parsed AVIF: 128x128 (8bpc)
   * First pixel: RGBA(255, 255, 255, 255)
