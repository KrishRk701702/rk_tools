import os

class AutoIncrement:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value_type": ("STRING", {"default": "INT", "options": ["INT", "FLOAT", "STRING"]}),
                "start_value": ("FLOAT", {"default": 1.0}),
                "step": ("FLOAT", {"default": 1.0}),
                "reset": ("BOOL", {"default": False}),
            }
        }
        
    RETURN_TYPES = ("INT", "FLOAT", "STRING",)
    FUNCTION = "increment"
    CATEGORY = "rk_tools"  # Updated to match your category

    def increment(self, value_type, start_value, step, reset):
        # Define the path to the state file
        state_file = os.path.join(os.path.dirname(__file__), f'current_value_{value_type}.txt')

        if reset or not os.path.exists(state_file):
            # Initialize the value
            if value_type == "INT":
                current_value = int(start_value)
            elif value_type == "FLOAT":
                current_value = float(start_value)
            elif value_type == "STRING":
                current_value = str(start_value)
        else:
            # Read the current value from the file
            with open(state_file, 'r') as f:
                current_value_str = f.read()
            if value_type == "INT":
                current_value = int(current_value_str)
            elif value_type == "FLOAT":
                current_value = float(current_value_str)
            elif value_type == "STRING":
                current_value = current_value_str

        # Increment the value
        if value_type == "INT":
            current_value += int(step)
            int_value = current_value
            float_value = float(current_value)
            string_value = str(current_value)
        elif value_type == "FLOAT":
            current_value += float(step)
            int_value = int(current_value)
            float_value = current_value
            string_value = str(current_value)
        elif value_type == "STRING":
            try:
                current_num = int(current_value)
                current_num += int(step)
                current_value = str(current_num)
            except ValueError:
                current_value = str(start_value)
            int_value = int(float(current_value))
            float_value = float(current_value)
            string_value = current_value

        # Save the updated value back to the file
        with open(state_file, 'w') as f:
            f.write(str(current_value))

        return (int_value, float_value, string_value)
