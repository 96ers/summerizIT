import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available")
    # Print CUDA device properties
    print(torch.cuda.get_device_properties(0))
else:
    print("CUDA is not available")
