fruits = [
    {"name": "apple", "calories": 130},
    {"name": "avocado", "calories": 50},
    {"name": "banana", "calories": 110},
    {"name": "grape", "calories": 60},
    {"name": "melon", "calories": 50},
]



def main():
    name = input("item: ")
    for l in fruits:
        if name in l["name"]:
            print("calories: ", l.get("calories", 0))    
       
        
main()