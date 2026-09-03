import json

def menu():
        print("\n ----Student Manegment----")
        print("1. Registration")
        print("2. display record")
        print("3. Exit")
        
        choice = int(input("Enter a choice: "))

        if choice == 1:
            student_registration

        elif choice == 2:
            display_record

        elif choice == 3:
            print("exit")
            
        
        else:
            print("invalid option")
            
listdata = []
def student_registration():
    dicdata ={}
    dicdata["id"]=int(input("please enter student id: "))
    dicdata["name"]=input("please enter name: ")
    dicdata["address"]=input("please enter student address: ")
    listdata.append(dicdata)
    print("Stuent Registration Successfully")

def display_record():
    for i in listdata:
        if listdata:
            print(i)


for n in range(2):
    menu()
    student_registration()
    display_record()



def save_file(data):
    with open("testiong.json","w") as file:
        jsonstring=json.dump(data)
        file.write(jsonstring)

def save_files(data):
    with open("testiong.json","r") as file:
        jsonstring=json.load(data)
        file.read(file)


    
# menu()
# for n in range(2):
#     menu()
#     student_registration()



# import json
# listdata =[]
# def registration():
   
#     student={}
#     student["id"] = int(input("\nplease enter student id: "))
#     student["name"] = input("please enter student name: ")
#     student["address"] = input("please enter student address: ")
#     listdata.append(student)

# for n in range(2):
#     registration()

# with open("data.json","a") as file:
#     json.dump(listdata, file)

    
