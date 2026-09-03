

students = []

def student_Registration():
    student={}
    student["Id"]=int(input("please enter your Id: "))
    student["Name"]=input("please enter your name: ")
    student["Address"]=input("please enter your address: ")
    students.append(student)
    print("Student Registration Successfully", student)

def Search_student():
    Id = int(input("\nEnter student Id Search: "))

    for student in students:
        if student["Id"] == Id:
            print(student)
            break
            
        print("student not found")

def Display_record():
    if not students:
        print("records found")
        return
    
    print("All student Recoards: ")
    for student in students:
        print(student)
        
def Remove_record():
    id = int(input("\nEnter student Id remove: "))

    for student in students:
        if student["Id"] == id:
            students.remove(student)
            print("Student remove successfully", student)
            return
    print("student not found")


