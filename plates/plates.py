def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    count = 0
    isnumber = 0

    for c in s:
        # nao pode ter menos que 2 caracteres
        if len(s) < 2:
            print("menor que 2 caracteres")
            return False

        # os dois primeiros caracteres nao podem ser numeros
        if count == 0 or count == 1:
            if c.isnumeric():
                print("é 0 ou 1 e é numerico")
                return False

        # nao pode ter mais que 6 caracteres
        if count > 5:
            print("é maior que5")
            return False

        # nao pode ter numeros no meio ex: AAA22A
        if s[-1].isnumeric() is False:
            if s[-2].isnumeric() is False:
                if s[-3].isnumeric():
                    print("numero no fim")
                    return False
            else:
                print("numero no fim")
                return False
        # o primeiro numero nao pode ter zero
        if c.isnumeric():

            if isnumber > 0:
                pass

            else:
                if int(c) == 0:
                    print("invalid zero")
                    return False

            isnumber += 1
        # nao pode ter caracteres especiais
        if s.isalnum() is False:
            print("tem pontos")
            return False

        count += 1
    else:
        return True


if __name__ == "__main__":
    main()
