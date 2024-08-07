def Converter(value, entry_scale, output_scale):
    entry_scale = entry_scale.lower()
    output_scale = output_scale.lower()

    if entry_scale == "celsius":
        if output_scale == "fahrenheit":
            return value * 1.8 + 32
        elif output_scale == "kelvin":
            return value + 273.15
        else:
            print("Invalid scale. Please try again.")

    elif entry_scale == "fahrenheit":
        if output_scale == "celsius":
            return (value - 32) / 1.8
        elif output_scale == "kelvin":
            return (value + 459.67) * 5 / 9
        else:
            print("Invalid scale. Please try again.")

    elif entry_scale == "kelvin":
        if output_scale == "fahrenheit":
            return value * 9 / 5 - 459.67
        elif output_scale == "celsius":
            return value - 273.15
        else:
            print("Invalid scale. Please try again.")
    else:
        print("Invalid scale. Please try again.")