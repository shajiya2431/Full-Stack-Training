class sweets:
    def chocolate(self):
        print("===chocolate name===")

class dary_milk(sweets):
    def chocolate(self):
        print("This is dary milk")

class kit_kat(sweets):
    def chocolate(self):
        self.name = "kit kat"
        print("this is kit kat")

class munch(sweets):
    def chocolate(self):
        self.name = "munch"
        print("this is munch")


ob=sweets()
ob.chocolate()

ob1=dary_milk()
ob1.chocolate()

ob2=kit_kat()
ob2.chocolate()

ob3=munch()
ob3.chocolate()
