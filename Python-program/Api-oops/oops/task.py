# class Signup:
#     def __init__(self):
#         self.name = "shajiya"
#         self.__number = 7209592431
#         self.__otp=1647

#     def get_function(self):
#         Name = input("please enter your name: ")
#         if Name == self.name:
#             print("Your Name:" ,self.name)

#         else:
#             print("Wrong name")
        

#     def set_function(self):
#         number = int(input("please enter your mobile number: "))
#         if number == self.__number:
#             print("Your OTP is:", self.__otp)
#         else:
#             print("Wrong Number")

# ob =Signup()
# ob.get_function()
# ob.set_function()

class signup:
    def __init__(self):
        self.name = "shajiya"
        self.__number = 9955469780
        self.__OTP = 2447

    def get_function(self):
        Name = input("please enter your name: ")
        # if Name == self.name:
        #     print("Your name:", self.name)
        # else:
        #     print("Wrong name ! please try again")

    def set_function(self):
        number = int(input("please enter your mobile number: "))
        if number == self.__number:
            print("Your OTP is:", self.__OTP)

        else:
            print("Wrong number")

ob = signup()
ob.get_function()
ob.set_function()

