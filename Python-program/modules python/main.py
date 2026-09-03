import Registration
import Search_student
import Remove_student
import Display_record

students = []

def menu():
    while True:
        print("\n~~~~ Student Management System ~~~~")
        print("1. Student Registration")
        print("2. Search Student")
        print("3. Display All Records")
        print("4. Remove Student")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            Registration.Registration(students)

        elif choice == 2:
            Search_student.Search_student_details(students)

        elif choice == 3:
            Display_record.Display_All_record(students)

        elif choice == 4:
            Remove_student.Remove_student_record(students)

        elif choice == 5:
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice! Try Again.")


menu()
