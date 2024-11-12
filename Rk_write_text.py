from PIL import Image, ImageDraw, ImageFont
import numpy as np
import torch

class RkWriteText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "text": ("STRING", {"default": "Your text here"}),
                "position": ("TUPLE", {"default": (10, 10)}),
                "font_size": ("INT", {"default": 20}),
                "font_color": ("TUPLE", {"default": (255, 255, 255)}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "write_text"
    CATEGORY = "rk_tools"  # Updated category

    def write_text(self, image, text, position, font_size, font_color):
        image = image.squeeze(0).numpy()
        pil_image = Image.fromarray((image * 255).astype(np.uint8))
        draw = ImageDraw.Draw(pil_image)
        font = ImageFont.load_default()
        draw.text(position, text, font=font, fill=font_color)
        image = np.array(pil_image).astype(np.float32) / 255.0
        return (torch.from_numpy(image).unsqueeze(0),)
