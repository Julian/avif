import os

import attr

from _avif import ffi, lib


class AVIFError(Exception):
    pass


def _succeed(avif_result):
    """
    Raise an exception if a ``libavif`` library function failed.
    """

    if avif_result != lib.AVIF_RESULT_OK:
        c_string = lib.avifResultToString(avif_result)
        raise AVIFError(ffi.string(c_string).decode("utf-8"))


def _avifDecoder():
    """
    Create an FFI-managed avifDecoder.
    """

    return ffi.gc(lib.avifDecoderCreate(), lib.avifDecoderDestroy)


@attr.s
class Decoder:
    """
    An AVIF decoder.
    """

    _decoder = attr.ib(factory=_avifDecoder)

    def parse_path(self, path):
        _succeed(lib.avifDecoderSetIOFile(self._decoder, os.fsencode(path)))
        _succeed(lib.avifDecoderParse(self._decoder))
        return self._decoder.image

    def next_images(self):
        while lib.avifDecoderNextImage(self._decoder) == lib.AVIF_RESULT_OK:
            yield self._decoder.image
