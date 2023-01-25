def main():
    x = input(">:")
    y = x.replace(x[5:], "")
    print(value(y))


def value(greeting):
    greeting = greeting.title().replace(",", "")
    if greeting[0] == "H" and greeting != "Hello":
        return "$20"

    elif greeting[0:5] == "Hello":
        return "$0"

    else:
        return "$100"


if __name__ == "__main__":
    main()


"""
greeting = input("?").title()


if greeting == "Hello":
    print("$0")

elif greeting[0] == "h":
    print("$20")
    
"""
