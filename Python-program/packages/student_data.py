import json
import os
listdata =[]
def registration():
   
    student={}
    student["id"] = int(input("\nplease enter student id: "))
    student["name"] = input("please enter student name: ")
    student["address"] = input("please enter student address: ")
    listdata.append(student)



for n in range(2):
    registration()

def file():

    with open("data.json","r") as file:
        olddata = json.load(file)
    olddata.extend(listdata)

    with open("data.json","w") as file:
        json.dump(olddata,file,indent=4)

    print("\nread json data")

json_string = json.dumps(listdata,indent = 4)
print(json_string)



    
