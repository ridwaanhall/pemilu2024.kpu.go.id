import os

from base.base import OptionHandler

def clear_screen():
    """
    Function to clear the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    option_handler = OptionHandler()

    while True:
        clear_screen()
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
        print("| 8. Exit                                |")
        print("+========================================+")

        option = input("Enter your choice: ")

        if option == '8':
            print("Exiting...")
            break

        option_handler.perform_option(option)
        input("\nPress Enter to continue...")
