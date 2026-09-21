from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class RuntimeInfo:
    device: str
    pytorch_version: str


def detect_runtime() -> RuntimeInfo:
    if torch.backends.mps.is_available():
        device = "mps"
    elif torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"

    return RuntimeInfo(device=device, pytorch_version=torch.__version__)
