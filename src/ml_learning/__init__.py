from ml_learning.runtime import RuntimeInfo, detect_runtime

__all__ = ["RuntimeInfo", "detect_runtime"]


def main() -> None:
    runtime = detect_runtime()
    print(f"Python ML environment ready. PyTorch device: {runtime.device}")
