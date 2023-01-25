import re


def main():
    print(convert(input("Hours: ")))

pm = {"1": 13, "2": 14, "3": 15, "4": 16, "5": 17, "6": 18, "7": 19, "8": 20, "9": 21, "10": 22, "11": 23, "12": 00}
am = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 0, "11": 11, "12": 12}

def convert(s):
    #pattern 9:00 AM to 5:00 PM
    #pattern 9 AM to 5 PM
    match = re.search(r"(\d\d?)(:\d\d)? (\w\w) to (\d\d?)(:\d\d)? (\w\w)", s)
    
    if match:
        if match.group(3) == "PM" and match.group(6) == "AM":
            #do something
            if match.group(1) in pm:
                if match.group(2) == None:
                    return f"{pm[match.group(1)]}:00 to {int(match.group(4)):02}:00" #verificar o 02
                else:
                    return f"{pm[match.group(1)]}{match.group(2)} to {match.group(4)}{match.group(5)}"
        
        elif match.group(6) == "PM" and match.group(3) == "AM":
            #do something
            if match.group(4) in pm:
                if match.group(5) == None:
                    return f"{int(match.group(1)):02}:00 to {pm[match.group(4)]}:00"
                else:
                    return f"{match.group(1)}{match.group(2)} to {pm[match.group(4)]}{match.group(5)}"
        
        elif match.group(6) == "AM" and match.group(3) == "AM":
            #do something
            if match.group(4) in pm:
                if match.group(5) == None:
                    return f"{int(match.group(1)):02}:00 to {int(match.group(4)):02}:00"
                else:
                    return f"{match.group(1)}{match.group(2)} to {match.group(4)}{match.group(5)}"       
                           
        else:
            if match.group(4) in pm or match.group(1) in pm :
                if match.group(5) == None:
                    return f"{int(pm[match.group(1)]):02}:00 to {int(pm[match.group(4)]):02}:00"
                else:
                    return f"{pm[match.group(1)]}{match.group(2)} to {pm[match.group(4)]}{match.group(5)}"
                
        
    else:
        return False
    



if __name__ == "__main__":
    main()