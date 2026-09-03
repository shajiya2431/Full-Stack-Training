dicdata = [
    {"Id":101, "name": "shajiya", "address": "mirganj"},
    {"Id":102, "name": "goldy", "address": "mirganj"},
    {"Id":103, "name": "saloni", "address": "mirganj"}

]

name = input("please enter your name: ")

for dicdata in dicdata:
    if name== dicdata["name"]:
            print("record found")
            print(dicdata)
            break

else:
     print("record not found")