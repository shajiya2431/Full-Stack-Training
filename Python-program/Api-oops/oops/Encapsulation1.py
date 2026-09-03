class mobile:
    def I_phone(self):
        self.brand = "I phone"
        self.price = 100000
        print("I phone:",self.price)
        
class Android:
    def Vivo(self):
        self.brand = "Vivo "
        self.price = 20000
        print("Vivo:",self.price)
        
class Sumsung(mobile,Android):
    def sumsung_galaxy(self):
        self.brand = "sumsung_galaxy"
        self.price = 40000
        print("sumsung galaxy:", self.price)
    
ob = Sumsung()
ob.Vivo()
ob.I_phone ()
ob.sumsung_galaxy()