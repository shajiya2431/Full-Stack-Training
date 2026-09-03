def Search_student_details(students):
    student_id = int(input("Enter student Id to search: "))

    for student in students:
        if student["Id"] == student_id:
            print("Student Found:")
            print(f"ID: {student['Id']}")
            print(f"Name: {student['Name']}")
            print(f"Address: {student['Address']}")
            return

    print("Student not found")
