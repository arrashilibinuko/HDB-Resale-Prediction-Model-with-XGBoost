import requests
import pandas as pd
import re

# Custom excel sheet, data of stations collected from wesite
mrt_search_list = pd.read_csv('mrt_searchval.csv')
# Add in a column mrt_name, which concatenates the mrt_station and "MRT STATION"
mrt_search_list['mrt_search_name'] = mrt_search_list.apply(lambda row: row['mrt_station'] + " STATION " + row['stn_code'], axis=1)


mrt_search_name_list = mrt_search_list['mrt_search_name'].tolist()
mrt_station_name_list = mrt_search_list['mrt_station'].tolist()

# Loop through the stn_code_list, request data from OneMap API and store the data in a list
mrt_list = []

index = 0
num_found = 0
num_not_found = 0
for mrt_search_name in mrt_search_name_list:
    print(f"Processing {mrt_search_name}")
    search_url = f"https://www.onemap.gov.sg/api/common/elastic/search?searchVal={mrt_search_name}&returnGeom=Y&getAddrDetails=Y"
    headers = {"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxYjVmMjE5NWJlOTA4YmFjNzdhMjdjYjVhNmJlNWMwZSIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC1uZXctMTYzMzc5OTU0Mi5hcC1zb3V0aGVhc3QtMS5lbGIuYW1hem9uYXdzLmNvbS9hcGkvdjIvdXNlci9wYXNzd29yZCIsImlhdCI6MTczNTk5NzU3OCwiZXhwIjoxNzM2MjU2Nzc4LCJuYmYiOjE3MzU5OTc1NzgsImp0aSI6InBFajlWVHo0TXBzN3lBdUsiLCJ1c2VyX2lkIjo1NTExLCJmb3JldmVyIjpmYWxzZX0.nm3jHOhifow5FuqjuPQzB3ag8i0v8nLGgFcOXFqDtjM"}
    response = requests.get(search_url, headers=headers)
    data = response.json()
    
    # This functions loops through data and searches for the first result that has a "SEARCHVAL" key with the value containing stn_code at the start
    found = False
    if(int(data['found']) > 1):
        for result in data['results']:
            pattern = re.compile(rf'^{re.escape(mrt_station_name_list[index])} (MRT|LRT) STATION.*', re.IGNORECASE)
            if pattern.match(result["SEARCHVAL"]):
                print("FOUND", result["SEARCHVAL"])
                mrt_list.append(result)
                found = True
                num_found += 1
                break
    else:
        print("FOUND", data['results'][0]["SEARCHVAL"])
        mrt_list.append(data['results'][0])
        found = True
        num_found += 1

    if not found:
        print("NOT FOUND ", mrt_search_name)
        num_not_found += 1
    print("")
    index += 1

# Convert to DataFrame
df = pd.DataFrame(mrt_list)

# Output to CSV
df.to_csv('mrt_list.csv', index=False)

print("Data has been written to mrt_list.csv, Found:", num_found, ", Not Found:", num_not_found)
