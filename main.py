import requests


# <--- GETTING PRICE OF DESIRED ITEM ON SKINPORT --->
class Skinport:
    def __init__(self):
        pass

    def GetSkinportDB(self):
        r = requests.get("https://api.skinport.com/v1/items", params={
        "app_id": 730,
        "currency": "PLN",
    })
        self.data=r.json()

    def GetWantedItem(self, name):
        
        selected = None

        for items in self.data:
            if items.get('market_hash_name') == name:
                selected = items
                break
          
        if selected: 
            min_price = selected.get("min_price")
            if min_price != None:
                return min_price
        else:
            return "Price / item not found."
        

# <--- GETTING PRICE OF DESIRED ITEM ON BUFF163 --->

#code


def main():
    skinport_api = Skinport()
    skinport_api.GetSkinportDB()
    lookingfor = input(str("Input full codename of searching item: "))
    price = skinport_api.GetWantedItem(lookingfor)

    if price != None:
        print(f"{lookingfor}: {price}")
    else:
        print("Item / price information not found.")

if __name__ == "__main__":
    main()
