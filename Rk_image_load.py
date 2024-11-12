import os
import numpy as np
from PIL import Image
import torch

class RkImageLoad:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image_path": ("STRING", {"default": "path/to/your/image.png"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "load_image"
    CATEGORY = "rk_tools"  # Updated category

    def load_image(self, image_path):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at: {image_path}")
        image = Image.open(image_path).convert("RGB")
        image = np.array(image).astype(np.float32) / 255.0
        return (torch.from_numpy(image).unsqueeze(0),)
