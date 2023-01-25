def main():
    
    x = input("fuel level: ")
    print(convert(x))
 
    
def convert(tank):
    sep = tank.split("/")
    
    try:
        sep = int(sep[0]) / int(sep[1])
        return gauge(sep) 
        
                    
    except ZeroDivisionError:
        print("zerooooooooo")
        
    except ValueError:
        print("teste")
        
def gauge(percentage):
          
    if percentage == 0:
        
        return "E"
            
    if percentage >= 0.25 and percentage < 0.5:
        
        return "25%"
        
    if percentage >= 0.5 and percentage < 0.75:
        
        return "50%"
        
    if percentage >= 0.75 and percentage < 1:
        
        return "75%"
        
    if percentage == 1:
        
        return "F"
    
    if percentage > 1:
        main()
  
if __name__ == "__main__":
    main()

