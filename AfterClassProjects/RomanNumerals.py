class RomanConverter:
    NUM_MAP = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def int_to_roman(self, num: int) -> str:
        """Converts an integer to its Roman numeral representation."""
        if not (0 < num < 4000):
            return "Error: Number must be between 1 and 3999."
            
        roman_result = ""
        for value, symbol in self.NUM_MAP:
            while num >= value:
                roman_result += symbol
                num -= value
        return roman_result

if __name__ == "__main__":
    converter = RomanConverter()
    try:
        user_input = int(input("Enter an integer to convert (1-3999): "))
        result = converter.int_to_roman(user_input)
        print(f"The Roman numeral for {user_input} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")