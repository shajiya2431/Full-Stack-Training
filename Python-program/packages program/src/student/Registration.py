from src.student.data import Load_data,save_data
from uuid import uuid4


def student_registration():
    students = Load_data()
    
    student = {}
    student["Id"]=uuid4().hex[:4]
    
    name =input("please enter your name: ").strip()
    if not name:
        print("Name is required")
        return
    
    address = input("please enter your address: ").strip()
    if not address:
        print("Address is required")
        return
    
    student["Name"] = name
    student["Address"] = address
    
    students.append(student)
    save_data(students)
    
    print("Student Registration Successfully", student)
