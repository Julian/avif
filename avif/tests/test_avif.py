def test_it_imports():
    from avif import Decoder
    import _avif  # noqa: F401

    Decoder()
