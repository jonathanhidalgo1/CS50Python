def main():
    time = input("type time:")
    convert(time)


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
        
    if hours > 6 and hours < 9:
        print("Breakfast")

    elif hours > 11 and hours < 14:
        print("lunchtime")
        
    elif hours > 17 and hours < 20:
        print("dinner time")

if __name__ == "__main__":
    main()