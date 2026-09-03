students = []

number = int(input("please enter the number you want to registered: "))

if number == -1 and 0:
    print("please enter the correct number ")

elif number < 1 or number > 5:
    print("please enter correct value(1 to 5)")

else:
    for i in range(number):
        print("\nenter student details")

        
        student = {
            "id": int(input("enter student id: ")),
            "name": input("please enter student name: "),
            "address": input("please enter student address: ")
        }
        
        students.append(student)
        print("\nstudent registered sucessfully:")
   

       

