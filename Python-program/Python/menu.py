students = []

while True :
    print("\n1. Registration")
    print("2. Serch student record")
    print("3. Exit")

    choice = int(input("\nEnter a choice: "))

    if choice == 1:
        Id = int(input("Student Id: "))
        Name = input("Student Name: ")
        Address = input("Student Address: ")
        Email = input("Student Email: ")

        student={
            "Id": Id,
            "Name": Name,
            "Address": Address,
            "Email": Email
        }
        students.append(student)
        print("\n~~~Registration succsessfully~~~")

        
    elif choice == 2:
        student = int(input("Enter Id to serch: "))

        for s in students:
            if s["Id"] == student:
                print("\nId:",s["Id"])
                print("Name:",s["Name"])
                print("Address",s["Address"])
                print("Email:",s["Email"])
                break

        else:
         print("student not found")

    elif choice == 3:
        print("Exit")
        break

