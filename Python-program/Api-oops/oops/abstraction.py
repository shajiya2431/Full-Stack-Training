from abc import ABC, abstractmethod

class Mobile(ABC):

    @abstractmethod
    def ram(self):
        pass
    
    @abstractmethod
    def charging(self):
        pass

    @abstractmethod
    def network(self):
        pass

    @abstractmethod
    def camera(self):
        pass

class Vivo(Mobile):

    def ram(self):
        print("\n===Vivo Mobile Features===")
        print("\nVivo: 8gb RAM")

    def charging(self):
        print("Vivo: Fast Charging Supported")

    def network(self):
        print("Vivo: 5g network")

    def camera(self):
        print("Vivo: 64mp camera")

class Sumsung(Mobile):

    def ram(self):
        print("\n===Sumsung Mobile Features===")
        print("\nSumsung: 12gb RAM")

    def charging(self):
        print("Sumsung: Super Fast Charging")

    def network(self):
        print("Sumsung: 5g network")

    def camera(self):
        print("Sumsung: 108MPmp camera")


ob = Vivo()

ob.ram()
ob.charging()
ob.network()
ob.camera()

ob = Sumsung()

ob.ram()
ob.charging()
ob.network()
ob.camera()
