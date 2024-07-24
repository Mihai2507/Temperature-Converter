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


def main():
    print("~~~TEMPERATURE CONVERTER~~~")
    print("Available scales are: Celsius, Fahrenheit, Kelvin")
    while True:
        value = float(input("Enter your value, please:\n"))
        entry_scale = input("Enter your entry scale, please:\n").lower()
        output_scale = input("Enter your output scale, please:\n").lower()
        result = Converter(value, entry_scale, output_scale)
        if result is not None:
            print(f"The converted value is: {result}")
        choice = input("Would you like to convert another value? (y/n)").lower()
        if choice != "y":
            break


if __name__ == '__main__':
    main()
