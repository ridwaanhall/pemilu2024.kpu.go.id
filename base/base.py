import requests
from datetime import datetime

class DataFetcher:
    @staticmethod
    def get_data(url):
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
            data = DataFetcher.get_data(url)
            if data:
                # print(f"Data fetched successfully from URL {option}!")
                print(data)
            else:
                print(f"Failed to fetch data from URL {option}.")
        elif option == "4":
            self.names()
        elif option == "5":
            self.region()
        elif option == "7":
            self.total_statistics()
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

    def total_statistics(self):
        # url1 = self.urls["1"]
        # url3 = self.urls["3"]

        data1 = DataFetcher.get_data(self.urls["1"])
        data3 = DataFetcher.get_data(self.urls["3"])

        if data1 and data3:
            last_update    = FormattedDate(data3["ts"]).get_formatted_date()
            progress       = data3['progres']['progres']
            total_progress = data3['progres']['total']
            percent        = data3['chart']['persen']

            print("\nreal count - KPU")
            print(f"last update: {last_update}")
            print(f"Progress   : {progress:>6,} of {total_progress:>6,} TPS ({percent}% done)")

            total_votes = sum(data3['chart'][key] for key in data3['chart'] if key != 'persen')
            for key, value in data1.items():
                percent = data3['chart'][key] / total_votes * 100
                print(f"{value['nomor_urut']:01d}: {data3['chart'][key]:>10,} - {percent:.2f}%")
        
        else:
            print("Failed to fetch data from one of the URLs.")

    def names(self):
        data = DataFetcher.get_data(self.urls["1"])
        if data:
            # print numor_urut and nama
            print("\nNames of presidential candidate and vice presidential candidate:")
            for key, value in data.items():
                print(f"{value['nomor_urut']}: {value['nama']}")
        else:
            print("Failed to fetch data from URL 1.")

    def region(self):
        data = DataFetcher.get_data(self.urls["2"])
        if data:
            print("\nRegion:")
            for region in data:
                print(f"{region['kode']}: {region['nama']}")
        else:
            print("Failed to fetch data from URL 2.")
                
class FormattedDate:
    def __init__(self, date_string):
        self.date_string = date_string

    def get_formatted_date(self):
        date_object = datetime.strptime(self.date_string, "%Y-%m-%d %H:%M:%S")
        formatted_date = date_object.strftime("%d %B %Y %H:%M:%S WIB")
        return formatted_date