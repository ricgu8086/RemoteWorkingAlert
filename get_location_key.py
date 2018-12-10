import requests
import sys

import secrets
import config


# Postal Code Search GET
url = "http://dataservice.accuweather.com/locations/v1/postalcodes/search"

data = {
            'apikey': secrets.API_KEY,
            'q': config.POSTAL_CODE,
            'language': config.LANGUAGE,
            'details': config.DETAILS
        }

response = requests.get(url, data)

if response.status_code != 200:
    print("There was a failure calling the API:\n%s" % response.text)
    sys.exit(-1)

print("Possible location keys:\n\n")

for ind in range(len(response.json())):
    location_info = response.json()[ind]['Country']
    location_key = response.json()[ind]['Key']

    print("Country info: %s\nLocation key: %s" % (location_info, location_key))
