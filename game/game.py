import random


def main():
             
    guess_num()
        
    
def guess_num():
    while True:
        try:
            levels = int(input("level: "))
            break
            
        except ValueError:
            guess_num()
        
    main_num = random.randint(1, levels)    
    print("rand", main_num)
    
    while True:
        guess = int(input("guess: "))
        
        if guess > main_num:
            print("maior")
            
        elif guess < main_num:
            print("menor")
            
        elif guess == main_num:
            print("over")
            break
            
   

        
main()