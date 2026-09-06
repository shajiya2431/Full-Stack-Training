from src.student.data import Load_data, save_data
def Delete_student():
    id = input("\nEnter student Id Delete: ")

    students = Load_data()
    found = False
    for student in students:
        if student["Id"]==id:
            students.remove(student)

            save_data(students)
            print("Student Delete Successfully", student)
            found=True
            break

    if not found:
        print("Student Id not found")