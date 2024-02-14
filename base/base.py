import requests

class DataFetcher:
    @staticmethod
    def fetch_data_from_url(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            json_data = response.json()
            return json_data
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None

class OptionHandler:
    def __init__(self):
        self.urls = {
            "1": "https://sirekap-obj-data.kpu.go.id/pemilu/ppwp.json",
            "2": "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/0.json",
            "3": "https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp.json"
        }

    def perform_option(self, option):
        if option in self.urls:
            url = self.urls[option]
            data = DataFetcher.fetch_data_from_url(url)
            if data:
                print(f"Data fetched successfully from URL {option}!")
            else:
                print(f"Failed to fetch data from URL {option}.")
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
