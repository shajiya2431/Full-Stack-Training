students = []
def Registration():
    Id = int(input("Enter student Id: "))
    Name = input("Enter student Name: ")
    Address = input("Enter student Address: ")
    email = input("Enter student email: ")

    student = {
        "Id": Id,
        "Name": Name,
        "Address": Address,
        "Email": email
    }
    students.append(student)
    print("~~~Registration successfully~~~")


    #--------View Student Data---------
def  View_Student_data():
    if not students:
        print("no studentvrecord found")
    else:
        for i in students:
            print(i)

    #--------Serch student---------
def Search_student():
    Id = int(input("Enter student id serch: "))
    for i in students:
        if i["Id"]==Id:
            print("Student found: ",i)
            return
        print("Student no found")

    #---------Menu----------
def dashboard():
    while True:
        print("\n-----Menu-----")
        print("1. Student Registration ")
        print("2. View student data ")
        print("3.Search student record ")
        print("4. Exit")

        choice = int(input("\nEnter a choice: "))

        if choice == 1:
            Registration()
        elif choice == 2:
            View_Student_data()
        elif choice == 3:
            Search_student()
        elif choice == 4:
            print("Program Exit")
            break
        else:
            print("invalid choice")

dashboard()