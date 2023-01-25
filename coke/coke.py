def amount_due():
    total_amount = 50    
    for coin in range(total_amount):
        print("Amount Due:", total_amount)        
        bank_machine = int(input("insert Coin: "))  
        if bank_machine == 50 or bank_machine == 25 or bank_machine == 10 or bank_machine == 5:
            total_amount = total_amount - bank_machine      
        if total_amount <= 0 :
            break                    
        
        
        

    
amount_due()