vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def main():
    say = shorten(input("input: "))
    print(say)


def shorten(word):
    for c in word:
        if c in vowels:
            word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()
