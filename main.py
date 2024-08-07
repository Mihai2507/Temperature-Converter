from Converter import Converter


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
