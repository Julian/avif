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


Installation from PyPI
----------------------

``avif`` is available `via PyPI <https://pypi.org/project/avif/>`_, with
wheels built for many common platforms. It can be installed via your
favorite Python package manager, e.g.:

.. code-block:: sh

    $ pip install avif

Or if you want to use `Pillow <https://github.com/python-pillow/Pillow>`_ integration:

.. code-block:: sh

    $ pip install avif[pillow]


Installation from source
------------------------


To install this module from source you will need to compile ``libavif`` yourself.
If you want to make use of the decoder you will also need to compile one
(decoders/encoders can be compiled from ``libavif``).


**List of available AV1 decoders:**

- `aom <https://aomedia.googlesource.com/aom>`_ (recommended)
- `dav1d <https://code.videolan.org/videolan/dav1d>`_
- `libgav1 <https://chromium.googlesource.com/codecs/libgav1>`_
- `rav1e <https://github.com/xiph/rav1e>`_
- `svt <https://github.com/AOMediaCodec/SVT-AV1>`_

If you compile ``avif`` without an AV1 decoder you will get
``AVIFError: No codec available`` raised when you try to get a result,
but you will still be able to import python module.

The installation steps below show how to compile ``libavif`` with the ``aom``
decoder.


Platform-Specific Steps
^^^^^^^^^^^^^^^^^^^^^^^

- `Linux <INSTALL.linux.rst>`_
- `Windows <INSTALL.win.rst>`_


Examples
--------

Examples can be found under `examples
<https://github.com/Julian/avif/tree/main/examples>`_ directory.

You can use ``sample.avif`` if you don't have any avif encoded image
for testing.  Sample is 128x128 pixels in size and it's all white
*(RGBA: 255, 255, 255, 255)*.

**To test if library works properly you can run:**

.. code-block:: bash

    $ python examples/avif_example_decode_file.py examples/sample.avif

Correct output:

.. code-block:: bash

    Parsed AVIF: 128x128 (8bpc)
    * First pixel: RGBA(255, 255, 255, 255)

**Or to test Pillow plugin:**

.. code-block:: bash

    $ python examples/avif_example_pillow_decode_file.py examples/sample.avif

Correct output:

.. code-block:: bash

    Parsed AVIF: 128x128 (Mode: RGBA)
    * First pixel: RGBA(255, 255, 255, 255)
