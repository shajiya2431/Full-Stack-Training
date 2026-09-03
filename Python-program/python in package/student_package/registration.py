students = []

def student_registration():
    student = {}

    student["id"] = int(input("Please enter student id: "))
    student["name"] = input("Please enter student name: ")
    student["address"] = input("Please enter student address: ")

    students.append(student)

    # Save into file
    with open("students.txt", "a") as file:
        file.write(f"{student['id']},{student['name']},{student['address']}\n")

    print("Registration Successfully")


def Search_student():
    search_id = input("Enter student id to search: ")
    found = False

    with open("students.txt", "r") as file:
        for line in file:
            id, name, address = line.strip().split(",")

            if id == search_id:
                print("\n Student Found")
                print("Id:", id)
                print("Name:", name)
                print("Address:", address)
                found = True
                break

    if not found:
        print("Student not found")


def Display_record():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No Records Found")
                return

            print("\nAll Student Records:\n")
            for line in data:
                id, name, address = line.strip().split(",")
                print("Id:", id)
                print("Name:", name)
                print("Address:", address)
                print("-" * 25)

    except FileNotFoundError:
        print("No file found. Please register student first.")


def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Registration")
        print("2. Search Student")
        print("3. Display Record")
        print("4. Exit")

        choice = int(input("Select option: "))

        if choice == 1:
            student_registration()
        elif choice == 2:
            Search_student()
        elif choice == 3:
            Display_record()
        elif choice == 4:
            print("Exit Program")
            break
        else:
            print("Invalid Choice")


menu()
