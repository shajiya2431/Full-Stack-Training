from src.student.data import Load_data,save_data
def Update_Student():
    Id = input("\nEnter student Id to Update: ").strip()
    if not Id:
        print("Id is required")
        return
    
    students = Load_data()
    found = False

    for student in students:
        if student["Id"] == Id:
            print("\nStudent found Enter new Details")

            name = input("Enter new name: ").strip()
            if not name:
                print("Name cannot be empty")
                return
            
            address = input("Enter new address: ").strip()
            if not address:
                print("Address cannot be empty")
                return
            
            student["Name"] = name
            student["Address"] = address
            save_data(students)

            print("Student Update Successfully")
            found = True
            break

    if not found:
        print("student Id not found")