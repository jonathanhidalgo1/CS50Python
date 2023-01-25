import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    

def validate(ip):
    num = re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip)
    
    try:    
        if int(num.group(1)) <= 255 and int(num.group(2)) <= 255 and int(num.group(3)) <= 255 and int(num.group(4)) <= 255:              
            return True    
        else:
            return False
        
    except AttributeError:
        return False
        
    
if __name__ == "__main__":
    main()