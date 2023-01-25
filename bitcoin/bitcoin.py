import json
import requests
import sys

request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = request.json()

#print(json.dumps(x.json(), indent=2))

def main():
    convertion()


def bitcoin_curruncy():
    for k, v in o['bpi'].items():
        if "USD" in v["code"]:
            return float(v["rate"].replace(",",""))

    
def convertion():
    try:   
        math = float(sys.argv[1]) * bitcoin_curruncy()
        print(f"${math:,.4f}")
            
    except IndexError:
        print("missing command line")
        
    except ValueError:
        print("not a integer")
        
        
main()   
    
