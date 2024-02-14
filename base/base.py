import requests
from datetime import datetime

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
                # print(f"Data fetched successfully from URL {option}!")
                print(data)
            else:
                print(f"Failed to fetch data from URL {option}.")
        elif option == "4":
            self.fetch_and_display_data()
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

    def fetch_and_display_data(self):
        url1 = self.urls["1"]
        url3 = self.urls["3"]

        data1 = DataFetcher.fetch_data_from_url(url1)
        data3 = DataFetcher.fetch_data_from_url(url3)

        if data1 and data3:
            last_update = datetime.strptime(data3["ts"], "%Y-%m-%d %H:%M:%S").strftime("%d %B %Y %H:%M:%S WIB")
            print(f"\nlast update: {last_update}")
            print(f"Progress   : {data3['progres']['progres']:>6,} of {data3['progres']['total']:>6,} TPS ({data3['chart']['persen']}% done)")

            total_votes = sum(data3['chart'].values())
            for key, value in data1.items():
                percent = data3['chart'][key] / total_votes * 100
                print(f"{value['nomor_urut']:01d}: {data3['chart'][key]:>10,} - {percent:.2f}%")
        
        else:
            print("Failed to fetch data from one of the URLs.")
