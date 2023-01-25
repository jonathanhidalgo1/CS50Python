import sys
import random
from pyfiglet import Figlet

def main():    
    figlet = Figlet()
    # se tiver o nome da fonte fazer isso
    try:
        if "-f" in sys.argv[1] or "--f" in sys.argv[1]:        
            set_font = figlet.setFont(font=sys.argv[2])
            x = input("input: ")
            print(figlet.renderText(x))
            

        # se nao tiver o nome da fonte escolher aleatoriamente de dentro da lista de fontes    figlet.getFonts()
    except:
        
        set_font = figlet.setFont(font=random.choice(figlet.getFonts()))  
        x = input("input: ")
        print(figlet.renderText(x))      
        #print(random.choice(figlet.getFonts()))
            
            
    
    
    
main()





'''
def main():
    x = input("Input: ")
    print(render(x))
    
def render(text):
    return figlet.renderText(text)  
    


main()

'''