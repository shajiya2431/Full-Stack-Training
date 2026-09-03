# class drink:
#     def water(self):
#         self.water
#         print("This is water bottel")

# class jucies:
#     def name(self):
#         self.name = "mango jucies"
#         print("your mango jucies")

# class oil(drink, jucies):
#     def oil(self):
#         self.name = "furtun"
#         print("fortune")


# ob=oil()
# ob.name()
# ob.water()
# ob.oil()


class univercity:
    def univercity_name(self):
        self.name = "jpu univarsity chapra"
        print("College name:", self.name)

class student_details:
    def student(self):
        self.name = "shajiya"
        self.address = "nabiganj"
        self.age= 18
        print("\nStudent Details")
        print("student name:", self.name)
        print("student address:", self.address)
        print("student age:", self.age)

class result(univercity, student_details):
    def marks(self):
        self.hindi = 50
        self.english = 70
        self.urdu = 60
        self.computer = 90
        print("\n===All Subject Marks===")
        print("hindi marks:", self.hindi)
        print("english marks:", self.english)
        print("urdu marks:", self.urdu)
        print("computer marks:", self.computer)

ob=result()
ob.univercity_name()
ob.student()
ob.marks()
        

