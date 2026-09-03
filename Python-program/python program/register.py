def register_student(id, name, address):
    student = {
        "Id":id,
        "Name":name,
        "Address": address
    }
    return student

def display_student(student):
    print("student Id:", student["Id"])
    print("student name:", student["Name"])
    print("student address:", student["Address"])

data = register_student(101, "shajiya", "mirganj")
display_student(data)