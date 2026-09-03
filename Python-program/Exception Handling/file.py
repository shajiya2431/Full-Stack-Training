import datetime
import json

def addition():
    try:
        first = int(input("Entar first number: "))
        second = int(input("Enter second number: "))

        print(first + second)

    except Exception as e:
        print("error! Please enter only number")
        write_logs(str(e))

def write_logs(data):
    dicdata = {
            "error":data,
            "datetime":str(datetime.datetime.now()),
            "function_name":"addition",
            "first":"first",
            "second":"second"
        }
    with open("student.txt", "w") as file:
        json.dump(dicdata,file,indent=4)

        

addition()

