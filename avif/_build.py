from cffi import FFI

ffi = FFI()


ffi.set_source(
    "_avif",
    """
    #include "avif/avif.h"
    """,
    libraries=["avif"],
)

ffi.cdef(
    """
    typedef struct {
        // Image information
        uint32_t width;
        uint32_t height;
        uint32_t depth; // all planes must share this depth; if depth>8, all planes are uint16_t internally
        ...;
    } avifImage;

    typedef struct {
        avifImage * image;

        int imageIndex;                // 0-based
        int imageCount;                // Always 1 for non-sequences

        ...;
    } avifDecoder;

    typedef enum {
        AVIF_RESULT_OK = ...,
    } avifResult;

    const char * avifResultToString(avifResult result);

    typedef struct {
        uint32_t width;       // must match associated avifImage
        uint32_t height;      // must match associated avifImage
        uint32_t depth;       // legal depths [8, 10, 12, 16]. if depth>8, pixels must be uint16_t internally

        uint8_t * pixels;
        ...;
    } avifRGBImage;

    void avifRGBImageSetDefaults(avifRGBImage * rgb, const avifImage * image);

    void avifRGBImageAllocatePixels(avifRGBImage * rgb);
    void avifRGBImageFreePixels(avifRGBImage * rgb);

    avifResult avifImageRGBToYUV(avifImage * image, const avifRGBImage * rgb);
    avifResult avifImageYUVToRGB(const avifImage * image, avifRGBImage * rgb);

    avifDecoder * avifDecoderCreate(void);
    void avifDecoderDestroy(avifDecoder * decoder);

    avifResult avifDecoderSetIOMemory(avifDecoder * decoder, const uint8_t * data, size_t size);
    avifResult avifDecoderSetIOFile(avifDecoder * decoder, const char * filename);
    avifResult avifDecoderParse(avifDecoder * decoder);
    avifResult avifDecoderNextImage(avifDecoder * decoder);
    """,
)


if __name__ == "__main__":
    ffi.compile()
