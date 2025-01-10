import requests
import pandas as pd

searchTerms = ['mall', 'shopping+centre', 'shopping']
shoppingMallList = []

commonUrl = "https://www.onemap.gov.sg/api/common/elastic/search?searchVal="
lastUrl = "&returnGeom=Y&getAddrDetails=Y&pageNum="
headers = {"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxYjVmMjE5NWJlOTA4YmFjNzdhMjdjYjVhNmJlNWMwZSIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC1uZXctMTYzMzc5OTU0Mi5hcC1zb3V0aGVhc3QtMS5lbGIuYW1hem9uYXdzLmNvbS9hcGkvdjIvdXNlci9wYXNzd29yZCIsImlhdCI6MTczNTk5NzU3OCwiZXhwIjoxNzM2MjU2Nzc4LCJuYmYiOjE3MzU5OTc1NzgsImp0aSI6InBFajlWVHo0TXBzN3lBdUsiLCJ1c2VyX2lkIjo1NTExLCJmb3JldmVyIjpmYWxzZX0.nm3jHOhifow5FuqjuPQzB3ag8i0v8nLGgFcOXFqDtjM"}


for searchTerm in searchTerms:
    url = commonUrl + searchTerm + lastUrl + "1"
    response = requests.get(url, headers=headers)
    data = response.json()

    numPages = int(data["totalNumPages"])
    for i in range(1, numPages+1):
        url = commonUrl + searchTerm + lastUrl + str(i)
        response = requests.get(url, headers=headers)
        data = response.json()
        shoppingMallList.extend(data["results"])

# Revmove entries with SEARCH VAL containing "ATM"
shoppingMallList = [mall for mall in shoppingMallList if "ATM" not in mall["SEARCHVAL"]]

# Remove duplicates in shoppingMallList that contains the same BUILDING
uniqueShoppingMallList = {mall['BUILDING']: mall for mall in shoppingMallList}.values()
shoppingMallList = list(uniqueShoppingMallList)

# Convert to DataFrame and export to CSV as shopping_mall_list.csv
df = pd.DataFrame(shoppingMallList)
df.to_csv('shopping_mall_list.csv', index=False)
