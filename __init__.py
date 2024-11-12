from .Rk_image_load import RkImageLoad
from .Rk_write_text import RkWriteText
from .Rk_show_any import RkShowAny
from .AutoIncrement import AutoIncrement  # Import the new node

NODE_CLASS_MAPPINGS = {
    "RkImageLoad": RkImageLoad,
    "RkWriteText": RkWriteText,
    "RkShowAny": RkShowAny,
    "AutoIncrement": AutoIncrement,  # Map the node
}
