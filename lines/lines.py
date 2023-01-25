import sys

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()   
        
    count = 0
    
    for line in lines:
        line = line.strip()
        if line[0:] == "":
            count -= 1
            
        elif "#" in line:
            
            count -= 1
        count += 1
    print(count)
except FileNotFoundError:
    print("file not found")
    
except IndexError:
    print("few arguments")