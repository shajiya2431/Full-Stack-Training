from src.student.data import Load_data, save_data
def View_Student_Record():
    students = Load_data()

    if not students:
        print("No student record found")
        return
    
    print("\n~~~~Student Recoards~~~~\n")
    for student in students:
        print("Id:", student["Id"])
        print("Name:", student["Name"])
        print("Address:", student["Address"])
        

    else:
        print("not found")
    
