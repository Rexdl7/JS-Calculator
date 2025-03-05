class bank:
    
    balance = 0
    ruuning = True
    
    def show_balance():
        print(f'Your current balance is {balance} rs')
        
    def deposit():
        pass
    
    def withdraw():
        pass
    
    def exit():
        running = False
        
    def instructions():
          print("1. Show Balance")
          print("2. Deposit")
          print("3. Withdraw")
          print("4. Exit")
        
    def main():
        if running:
            choice = int(input("Choose something from the above: "))
        
            if choice == 1:
                show_balance()
            
            if choice == 2:
                deposit()
            
            if choice == 3:
                withdraw()
            
            if choice == 4:
                exit()
            main()
        