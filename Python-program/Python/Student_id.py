Id =  int(input("enter student id: "))

students = {
    
    30: {
        "Name": "goldy kumari",
        "Address": "mirganj",
        "College": "kamla rai college",
        "Course" : "BSC",
        "Email Id": "g@gmail.com"
    },

    12: {
        "Name": "neha kumari",
        "Address": "mirganj",
        "College": "Gopeshwar college",
        "Course": "BA",
        "Email Id": "n@gmail.com"
    },

    40: {
        "Name": "saloni kumari",
        "Address": "mirganj",
        "College": "kamla rai college",
        "Course": "B Tech",
        "Email Id": "s@gmail.com"
    }
}

if Id in students:
    print("\n*****student details*****")
    print("Name:",students[Id]["Name"])
    print("Address:",students[Id]["Address"])
    print("College:",students[Id]["College"])
    print("Course:",students[Id]["Course"])
    print("Email Id:",students[Id]["Email Id"])

else:
    print("student id not found")


