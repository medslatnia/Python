class Car:

    def __init__(self):
        self.gas_liter = 100

    def display_tank(self):
        print(f"The car contains {self.gas_liter} of gas ")
        
    def roule(self, km):
        
        self.gas_liter -= (km * 5)/100
        if self.gas_liter <= 0:
            print("You're out of gas, fill up! ")
            return

        elif (self.gas_liter > 0 ) and (self.gas_liter <= 10):
            print("You're almost out of gas, fill up! ")
            

        
        self.display_tank()

    def faire_leplein(self):
        self.gas_liter = 100
        print("You can leave! ")
        
v = Car()
v.roule(100)
