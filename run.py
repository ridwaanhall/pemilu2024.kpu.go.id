from base.base import OptionHandler

if __name__ == "__main__":
    option_handler = OptionHandler()

    print("Welcome to pemilu 2024!")
    print("Choose an option:")
    print("1. Fetch data from URL 1")
    print("2. Fetch data from URL 2")
    print("3. Fetch data from URL 3")
    print("4. Display data from URL 1 and URL 3")

    option = input("Enter your choice (1, 2, 3, or 4): ")

    option_handler.perform_option(option)
