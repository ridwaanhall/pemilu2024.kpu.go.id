import requests
from fake_useragent import UserAgent

'''
this code is for testing. 403 - Forbidden fixed.
'''

url = "https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp.json"

# Create a UserAgent object
ua = UserAgent()

headers = {
    "User-Agent": ua.random,
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

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    json_data = response.json()  # Convert response to JSON format
    print(json_data)  # Print the JSON data

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
