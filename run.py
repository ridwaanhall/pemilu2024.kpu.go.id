from base.base import OptionHandler

if __name__ == "__main__":
    option_handler = OptionHandler()

    print("+========================================+")
    print("|  Welcome to pemilu 2024! (real count)  |")
    print("+========================================+")
    print("| Choose an option:                      |")
    print("| 1. Fetch data from URL 1 - json        |")
    print("| 2. Fetch data from URL 2 - json        |")
    print("| 3. Fetch data from URL 3 - json        |")
    print("+----------------------------------------+")
    print("| 4. names of capres and cawapres        |")
    print("| 5. region                              |")
    print("| 6. regional statistics                 |")
    print("+----------------------------------------+")
    print("| 7. total statistics                    |")
    print("+========================================+")

    option = input("Enter your choice: ")

    option_handler.perform_option(option)
