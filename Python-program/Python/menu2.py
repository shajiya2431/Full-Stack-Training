x = int(input("please enter first number: "))
y = int(input("please enter second number: "))

def multiply(x,y):
    print(x*y)

def division(x,y):
    print(x/y)


def menu():
    print("\n1. multiply ")
    print("2. division ")
    option = int(input("\nplease enter a number: "))
    return option


def dashboard():
    number = menu()
    if number ==1:
        multiply(x,y)

    elif number ==2:
        division(x,y)

dashboard()



# def menu():
#     print("1. multiply")
#     print("2. division")
#     option = int(input("please enter a number: "))
#     return option

# def multiply(x,y):
#     print(x*y)

# def division(x,y):
#     print(x/y)

# def dashboard():
#     number =menu()
#     x= int(input("please enter first number: "))
#     y= int(input("please enter second number: "))

#     if number ==1:
#         multiply(x,y)

#     elif number ==2:
#         division(x,y)



# dashboard()