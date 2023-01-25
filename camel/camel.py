def main():
    variable = input("CamelCase: ")
    snake_case(variable)
    
def snake_case(name):
    for c in name:
        if c.isupper():
            name = name.replace(c,f"_{c.lower()}")
    print(name)
        
    
main()