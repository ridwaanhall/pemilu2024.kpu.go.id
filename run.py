from base.base import OptionHandler

if __name__ == "__main__":
    option_handler = OptionHandler()

    print("+----------------------------------------+")
    print("|  Welcome to pemilu 2024! (real count)  |")
    print("+----------------------------------------+")
    print("| Choose an option:                      |")
    print("| 1. Fetch data from URL 1               |")
    print("| 2. Fetch data from URL 2               |")
    print("| 3. Fetch data from URL 3               |")
    print("| 4. Total statistics                    |")
    print("| 5. names of capres and cawapres        |")
    print("+----------------------------------------+")

    option = input("Enter your choice (1, 2, 3, or 4): ")

    option_handler.perform_option(option)
