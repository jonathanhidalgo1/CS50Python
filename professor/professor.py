import random

def main():
    get_level()


def get_level():
    
    level_list=[1,2,3]
    try:
        x = int(input("level: "))
        if x in level_list:
            generate_integer(x)
        else:
            main()
            
    except ValueError:
        get_level()


def generate_integer(level):
    
    count = 0 
    score = 10
    
        
    while count < 10:
        
        #variaveis para randomizar numeros da soma
        nums1 = random.randint(1, 10)
        nums2 = random.randint(1, 10)
        #level do jogo
        lev = nums1 * level
        #variavel para checar condicao
        some = nums1 + lev
        try:
            
        #input do usuario
            math = int(input(f"{nums1} + {lev} = "))
            
        except ValueError:
            print("EEE")
            math = int(input(f"{nums1} + {lev} = "))
            
        
        
        #se o resultado do usuario for diferente da variavel some printa "EEE"
        if math != some:
            count2 = 0
            score -= 1
            print("EEE")
            while count2 < 3:
                
                if math != some:
                    math = int(input(f"{nums1} + {lev} = "))
                    print("EEE")
                else:
                    break
                count2 += 1
                
            print(f"{nums1} + {lev} = ", nums1 + lev)
        '''
        1-Answer the first question incorrectly, three times. Your program should output the correct answer. 
        2-Your program should output 10 distinct problems before printing the number of questions you answered correctly and exiting.
        '''  
                
        count += 1
    print(score)
    
     

if __name__ == "__main__":
    main()