import csv
import sys

try:
    if len(sys.argv) > 3:
        print("too many arguments")
        sys.exit
    else:
        with open(sys.argv[2], "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name","lastname","house"])
            writer.writeheader()

        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
                
            for row in reader:
                clean = row["name"]
                clean = clean.split(',')
                name = clean[1]
                lastname = clean[0]
                
                        
                with open(sys.argv[2], "a", newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=["name","lastname","house"])            
                    writer.writerow({"name": name, "lastname": lastname, "house": row["house"]})
                

except FileNotFoundError:
    print("file not found")
    
except IndexError:
    print("too few arguments")
