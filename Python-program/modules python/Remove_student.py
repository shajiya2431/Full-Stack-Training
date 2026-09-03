def Remove_student_record(students):
    student_id = int(input("Enter student Id to remove: "))

    for student in students:
        if student["Id"] == student_id:
            students.remove(student)
            print("Student removed successfully")
            return

    print("Student not found")
