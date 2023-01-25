
def main():
    x = input(">")
    if "+" in x:
        separator_plus(x)
        
    elif "-" in x:
        separator_minor(x)
        
    elif "*" in x:
        separator_multiply(x)
        
    elif "/" in x:
        separator_division(x)
        
    
def separator_plus(y):
    sep = y.split("+")
    calc = int(sep[0]) + int(sep[1])
    print(calc)
    
def separator_minor(y):
    sep = y.split("-")
    calc = int(sep[0]) - int(sep[1])
    print(calc)    
    
def separator_multiply(y):
    sep = y.split("*")
    calc = int(sep[0]) * int(sep[1])
    print(calc)    
    
def separator_division(y):
    sep = y.split("/")
    calc = int(sep[0]) / int(sep[1])
    print(calc)   
    


main()



'''
x = input(">")
y = x.split("+")
calc = int(y[0]) + int(y[1])
print(calc)
'''