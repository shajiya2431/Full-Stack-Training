from student_package.registration import student_registration, Search_student, Display_record
def menu():
    while True:
        print("\n1. Registration")
        print("2. Search Student")
        print("3. Display Record")
        print("4. Exit")

        choice = int(input("Enter a choice: "))

        if choice == 1:
            student_registration()

        elif choice == 2:
            Search_student()

        elif choice == 3:
            Display_record()
            
        elif choice == 4:
            print("program exit")
            break

        else:
            print("Invalid option")