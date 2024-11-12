class RkShowAny:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "data": ("ANY",),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "show_any"
    CATEGORY = "rk_tools"  # Updated category

    def show_any(self, data):
        print("Data:", data)
        return ()
