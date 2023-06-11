import os

import attr

from _avif import ffi, lib


class AVIFError(Exception):
    pass


def _succeed(avif_result: int):
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

    def parse_path(self, path: str):
        _succeed(lib.avifDecoderSetIOFile(self._decoder, os.fsencode(path)))
        _succeed(lib.avifDecoderParse(self._decoder))
        return self._decoder.image

    def parse_data(self, data: bytes):
        _succeed(lib.avifDecoderSetIOMemory(self._decoder, data, len(data)))
        _succeed(lib.avifDecoderParse(self._decoder))
        return self._decoder.image

    def next_images(self):
        while True:
            res = lib.avifDecoderNextImage(self._decoder)
            if res == lib.AVIF_RESULT_NO_IMAGES_REMAINING:
                break
            _succeed(res)
            yield self._decoder.image

    def nth_image(self, n: int):
        _succeed(lib.avifDecoderNthImage(self._decoder, n))

        return self._decoder.image
