class food():
    def show_info(self):
        print("This is food Item")

class pizza(food):
    def name(self):
        price = 300
        print("pizza Price:", price)
        

class burgar(pizza):
    def food_name(self):
        price = 30
        print("Burgar Price:", price)

ob=burgar()
ob.show_info()
ob.name()
ob.food_name()




