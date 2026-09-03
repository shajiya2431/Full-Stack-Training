class Student:
    def __init__(self):
        self.Id = int(input("Please Enter Your Id: "))
        self.Name = input("Please Enter Your Name: ")
        self.Address = input("Please Enter Your Address: ")
        

    def Display_student_data(self):
        print("\nDisplay Student Record")
        print(self.Id)
        print(self.Name)
        print(self.Address)
        
ob=Student()
ob.Display_student_data()

    

    