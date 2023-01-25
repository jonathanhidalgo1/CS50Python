menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0
    try:    
        while True:
            try:
                prompt = input("Item: ")    
                verify = check(prompt)
                total = total + check(prompt)
                print(f"$",total)
            except TypeError:
                pass
    except KeyboardInterrupt:
        pass
    
        
        
def check(name):    
    if name in menu:
        return menu[name]
    else:
        pass
       
        
    
    
















main()