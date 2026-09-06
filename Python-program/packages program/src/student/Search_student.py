from src.student.data import Load_data,save_data
def Search_Student():
    students = Load_data()
    Id = input("\nPlease enter Id: ").strip()

    if not Id:
        print("Id is required!")
        return

    found = False

    for student in students:
        if student["Id"] == Id:
            print("student found:", student)
            found = True
            break

    if not found:
        print("student not found")
