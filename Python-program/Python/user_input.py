def user():
    id = int(input("Enter id: "))
    name = input("Enter name: ")
    return id,name
    

def output():
    data = user()
    print(data)

output()
