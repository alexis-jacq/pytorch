import torch

while True:
    try:
        torch.Tensor(5000, 5000)[1, 'a']
    except Exception:
        pass
