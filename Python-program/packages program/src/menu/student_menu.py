from src.student.Registration import student_registration
from src.student.Search_student import Search_Student
from src.student.update_student import Update_Student
from src.student.Delete_Student import Delete_student
from src.student.View_student import View_Student_Record


def menu():
    while True:
        print("\n====Student Managment System====")
        print("1. Registration")
        print("2. Search student")
        print("3. Update Student Record")
        print("4. Delete student")
        print("5. View Student Record")
        print("6. Exit")

        option = int(input("\nplease select any option: "))

        if option == 1:
            student_registration()

        elif option == 2:
            Search_Student()

        elif option == 3:
            Update_Student()

        elif option == 4:
            Delete_student()

        elif option == 5:
            View_Student_Record()

        elif option == 6:
            print("Program close")
            break

        else:
            print("Invalid choice")




        
        
        

