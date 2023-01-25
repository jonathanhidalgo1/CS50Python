import csv
from tabulate import tabulate
import sys

pizza = []
try:
    
    if len(sys.argv) > 2:
        print("too many arguments")
        sys.exit
                   
    else:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizza.append({"Sicilian Pizza": row["Sicilian Pizza"], 
                            "Small": row["Small"],
                            "Large": row["Large"]})
                
                
            print(tabulate(pizza,headers="keys", tablefmt="grid"))
        
except FileNotFoundError:
    print("file not found")
    
except IndexError:
    print("too few arguments")