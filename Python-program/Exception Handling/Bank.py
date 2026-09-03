class Bank_Account:
    def __init__(self): 
        self.balance = 500

    def Add_amount(self):
        amount = int(input("Please enter add amount: "))
        self.balance += amount 
        print("Amount Add Successfully")
        print(self.balance)

    def With_Drow_Amount(self):
        amount = int(input("please enter with drow amount: "))
        if amount > self.balance:
            print("Insufficent amount")
            print("your balance:", self.balance)
        else:
            self.balance  -= amount
            print("Your Balance :", self.balance)

    def Check_balance(self):
        print("Your Balance is:", self.balance)
        
    
    def menu(self):
        while True:
            print("\n===Bank Menu===")
            print("1. Add Amount")
            print("2. With Drow Ammount")
            print("3. Check Balance")
            print("4. Exit")

            option = int(input("\nPlease enter any option: "))

            if option == 1:
                self.Add_amount()
            elif option == 2:
                self.With_Drow_Amount()
            elif option == 3:
                self.Check_balance()
                
            elif option == 4:
                print("Close program")
                break
            else:
                print("Invalid option")              
        
    
ob = Bank_Account()
ob.menu()




    
        