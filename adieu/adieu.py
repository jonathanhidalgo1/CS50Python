import inflect
p = inflect.engine()
names = []

while True:
    try:
        x = input('name: ')
        names.append(x)
        
    except KeyboardInterrupt:
        print("Adieu, adieu to ",p.join(names))
        break
        
    