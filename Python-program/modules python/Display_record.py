def Display_All_record(students):
    if not students:
        print("Records not found")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(f"ID: {student['Id']}, Name: {student['Name']}, Address: {student['Address']}")
