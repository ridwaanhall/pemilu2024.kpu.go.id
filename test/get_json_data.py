import requests
from fake_useragent import UserAgent

class DataFetcher:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": UserAgent().random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,mt;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Dnt": "1",
            "Host": "sirekap-obj-data.kpu.go.id",
            "Pragma": "no-cache",
            "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1"
        }

    def fetch_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

            print("Status Code:", response.status_code)
            print("Status Text:", response.reason)
            # print("Response Body:", response.text)

        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)

if __name__ == "__main__":
    url = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/0.json"
    data_fetcher = DataFetcher(url)
    data_fetcher.fetch_data()
