import json
students = []
while True:
    print("1. Registration")
    print("2. Display student record")
    print("3. Serch student")
    print("4. Exit")

    choice = int(input("\nEnter a choice: "))
    if choice == 1:
        Id = int(input("Student Id: "))
        Name = input("Student Name: ")
        Address = input("Student Address: ")
        Email = input("Student Email: ")

        Qualifications = []
        while True:
            student = input("do you want add more qualification yes/no: ")
            if student == "yes":
                course_name = input("Enter course name: ")
                passing_year = int(input("Enter passing year: "))

                Qualifications.append({
                "course_name": course_name,
                "passing_year": passing_year
                })
                
            elif student == "no":
                break
            else:
                print("type yes or no")


            student_data ={
                "Id": Id,
                "Name": Name,
                "Address": Address,
                "Email": Email,
                "Qualification": Qualifications
            }
            students.append(student_data)
            print("\n~~~Registration succsessfully~~~")

    elif choice == 2:
        for s in students:
            print(json.dumps(student,indent=4))
           
        
    elif choice == 3:
        student_id = int(input("Serch student: "))

        for i in students:
            if i["Id"] == student_id:
                print("\nId:",i["Id"])
                print("Name:",i["Name"])
                print("Address",i["Address"])
                print("Email:",i["Email"])
                print("Qualification:",i["Qualification"])
                found= True
                break

        else:
            print("student not found")


    elif choice == 4:
        print("Exit")
        break
    else:
        print("please select any choice: ")






                

                


    