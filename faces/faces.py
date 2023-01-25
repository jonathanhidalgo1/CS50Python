import emoji
def convert(say):
    
    say = say.replace(":)", emoji.emojize(':grinning_face:'))
    say = say.replace(":(", emoji.emojize(':neutral_face:'))
    
    print(say)
    


x = input("saysomething: ")   

convert(x)

