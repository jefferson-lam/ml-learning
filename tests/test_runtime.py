from ml_learning import detect_runtime


def test_detect_runtime_returns_supported_device() -> None:
    runtime = detect_runtime()

    assert runtime.device in {"cpu", "cuda", "mps"}
    assert runtime.pytorch_version
