from src.student.student_dashboard import student_Registration,Search_student,Display_record,Remove_record
def menu():
    while True:
        print("\n1. Registration")
        print("2. Search Student")
        print("3. Display Record")
        print("4. Remove Student")
        print("5. Exit")
        


        option=int(input("\nPlease select any option: "))

        if option==1:
            student_Registration()
        

        elif option==2:
        
            Search_student()

        elif option==3:
            Display_record()

        elif option==4:
            Remove_record()

        elif option==5:
            print("program exit")
            break
        
        
        else:
            print("Invalid choice")
        




    



