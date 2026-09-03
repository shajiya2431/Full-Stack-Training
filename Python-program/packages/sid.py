import json

list_data=[]

def Registration():

    data={}

    data["id"]=int(input("\nplease enter your id:"))
    data["name"]=input("please enter name:")
    data["address"]=input("please enter your address:")

    list_data.append(data)


for n in range(2):

    Registration()


with open("menu.json","w") as file:

    json.dump(list_data,file,indent=4)

with open("menu.json","r") as file:
    data = json.load(file)

print("\nread json data")

json_string = json.dumps(data, indent = 4)
print(json_string)