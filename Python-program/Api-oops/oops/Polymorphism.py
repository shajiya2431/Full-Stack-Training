class Online_Class:
    def join_class(self):
        print("\n===Online class Students===")


class Student(Online_Class):
    def join_class(self):
        print("Student join this class")

class Teacher(Online_Class):
    def join_class(self):
        print("Teachers start teaching")

class Admin(Online_Class):
    def join_class(self):
        print("Admin manages the class")


ob=Online_Class()
ob.join_class()


ob1=Student()
ob1.join_class()

ob2=Teacher()
ob2.join_class()

ob3=Admin()
ob3.join_class()
