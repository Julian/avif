from _avif import ffi, lib


class AVIFError(Exception):
    @classmethod
    def from_result(cls, avif_result):
        c_string = lib.avifResultToString(avif_result)
        return cls(ffi.string(c_string).decode("utf-8"))
