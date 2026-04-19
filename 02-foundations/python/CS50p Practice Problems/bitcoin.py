import sys
import requests

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=9e446636a7188638654577a3f8c6969454f8bd2e5b1c8f0a94d0eb0d59b96061"
    response = requests.get(url)
    json_response = response.json()

    btc_price = json_response["data"]["priceUsd"]
except requests.RequestException:
    sys.exit()


output = float(btc_price) * float(n)



print(f"${output:,.4f}")
