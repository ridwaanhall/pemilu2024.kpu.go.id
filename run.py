from base.base import OptionHandler

if __name__ == "__main__":
    option_handler = OptionHandler()

    print("Welcome to Data Fetcher!")
    print("Choose an option:")
    print("1. Fetch data from URL 1")
    print("2. Fetch data from URL 2")
    print("3. Fetch data from URL 3")

    option = input("Enter your choice (1, 2, or 3): ")

    option_handler.perform_option(option)
