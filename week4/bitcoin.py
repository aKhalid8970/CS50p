import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    factor = float(sys.argv[1])
except ValueError:
    sys.exit("Missing command-line argument")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except:
    sys.exit(1)
else:
    o = response.json()
    for result in o['bpi']:
        """
        x = (o['bpi']['USD']['rate']).replace(",", "")
        x = float(x)
        y = x * factor
        print(f"${y:,.4f}")
        sys.exit(0)
        """
        print(result)
