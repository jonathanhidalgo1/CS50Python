def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    tip = float(dollars_to_float(dollars)) * float(percent_to_float(percent))
    print(f"Leave ${tip / 100}")


def dollars_to_float(dollars):
    return dollars.replace("$","")
    


def percent_to_float(percent):
    return percent.replace("%","")


main()