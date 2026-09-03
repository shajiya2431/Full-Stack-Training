from system.Calculator.Calculator_dashboard import Add, Subtract, Multiply, Division
x = int(input("please enter first number: "))
y = int(input("please enter second number: "))

   
def menu():
    while True:
        print("\n~~~Calculator Menu~~~")
        print("1.Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")
        

        number = int(input("\nplease enter your choice: "))

        if number == 1:
            Add(x,y)

        elif number == 2:
            Subtract(x,y)

        elif number == 3:
            Multiply(x,y)

        elif number == 4:
            Division(x,y)

        elif number == 5:
            print("Program Exit")
            break

        else:
            print("Invalid choice")


        
