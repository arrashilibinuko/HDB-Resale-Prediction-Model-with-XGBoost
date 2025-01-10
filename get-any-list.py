import requests
import pandas as pd

url = "https://www.onemap.gov.sg/api/common/elastic/search?searchVal=266 Bishan St 24&returnGeom=Y&getAddrDetails=Y&pageNum=1"

headers = {"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxYjVmMjE5NWJlOTA4YmFjNzdhMjdjYjVhNmJlNWMwZSIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC1uZXctMTYzMzc5OTU0Mi5hcC1zb3V0aGVhc3QtMS5lbGIuYW1hem9uYXdzLmNvbS9hcGkvdjIvdXNlci9wYXNzd29yZCIsImlhdCI6MTczNTk5NzU3OCwiZXhwIjoxNzM2MjU2Nzc4LCJuYmYiOjE3MzU5OTc1NzgsImp0aSI6InBFajlWVHo0TXBzN3lBdUsiLCJ1c2VyX2lkIjo1NTExLCJmb3JldmVyIjpmYWxzZX0.nm3jHOhifow5FuqjuPQzB3ag8i0v8nLGgFcOXFqDtjM"}

response = requests.get(url, headers=headers)
data = response.json()


print(response.text)
