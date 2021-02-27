import requests

def MacAddressLookup(mac):
    url = ("https://macvendors.co/api/" + mac)
    response=requests.get(url)
    result=response.json()
    if result["result"]:
        final=result['result']
        if final["company"]:
            print("Company:" + final["company"])
        if final["address"]:
            print("Address:" + final["address"])
        if final["country"]:
            print("Country:" + final["country"])
        print("")
    else:
        print("Error: Something Went Wrong")
