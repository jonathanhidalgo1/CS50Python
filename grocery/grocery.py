values = 1
grocery_list = {}


def main():
       
    while True:
        try:
            item = input(" ").upper()
            x = check(item)
                       
        except KeyboardInterrupt:
            alpha_order = sorted(grocery_list.items())
            for k, j in alpha_order:
                print(j,k) 
            break
    
        
        
def check(name):
    if name in grocery_list:
        incremental = grocery_list.get(name) + 1
        grocery_list[name] = incremental
            
    else:
        grocery_list[name] = values
        
        
    


    
    
















main()