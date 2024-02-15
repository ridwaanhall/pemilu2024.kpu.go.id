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
        elif option == "6":
            self.regional_statistics()
        elif option == "7":
            self.total_statistics()
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

    def total_statistics(self):
        # url1 = self.urls["1"]
        # url3 = self.urls["3"]

        name_ppwp = DataFetcher.get_data(self.urls["1"])
        reg_stat = DataFetcher.get_data(self.urls["3"])

        if name_ppwp and reg_stat:
            last_update    = FormattedDate(reg_stat["ts"]).get_formatted_date()
            progress       = reg_stat['progres']['progres']
            total_progress = reg_stat['progres']['total']
            percent        = reg_stat['chart']['persen']

            print("\nreal count - KPU")
            print(f"last update: {last_update}")
            print(f"Progress   : {progress:>6,} of {total_progress:>6,} TPS ({percent}% done)")

            total_votes = sum(reg_stat['chart'][key] for key in reg_stat['chart'] if key != 'persen')
            for key, value in name_ppwp.items():
                percent = reg_stat['chart'][key] / total_votes * 100
                print(f"{value['nomor_urut']:01d}: {reg_stat['chart'][key]:>10,} - {percent:.2f}% ({value['nama']})")
        
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

    def regional_statistics(self):
        reg_name = DataFetcher.get_data(self.urls["2"])
        reg_stat = DataFetcher.get_data(self.urls["3"])

        for key, value in reg_stat['table'].items():
            for reg in reg_name:
                if reg['kode'] == key:
                    print(f"\n{key}. {reg['nama']} - level:{reg['tingkat']}")
                    print(f"progress: {value['persen']}%")
                    for k, v in value.items():
                        if k != 'status_progress' and k != 'persen' and k !='psu':
                            print(f"{k}: {v:>10,}")

                
class FormattedDate:
    def __init__(self, date_string):
        self.date_string = date_string

    def get_formatted_date(self):
        date_object = datetime.strptime(self.date_string, "%Y-%m-%d %H:%M:%S")
        formatted_date = date_object.strftime("%d %B %Y %H:%M:%S WIB")
        return formatted_date