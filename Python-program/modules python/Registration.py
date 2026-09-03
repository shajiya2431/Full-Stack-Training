def Registration(students):
    data = {}

    data["Id"] = int(input("Please enter student Id: "))
    data["Name"] = input("Please enter student Name: ")
    data["Address"] = input("Please enter student Address: ")

    students.append(data)

    print("Student Registered Successfully")
