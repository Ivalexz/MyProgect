class Appliance:
    def __init__(self,brand):
        self.brand = brand

    def get_info(self):
        print(f"Бренд приладу:{self.brand}", end=" ")


class KitchenAppliance(Appliance):
    def __init__(self, brand, power):
        super().__init__(brand)
        self.power  = power
        
    def get_info(self):
        super().get_info()
        print(f" Потужність: {self.power}", end=" ")

class Oven(KitchenAppliance):
    def __init__(self, brand, power, temperature_range):
        super().__init__(brand, power)
        self.temperature_range = temperature_range
        
    def get_info(self):
        super().get_info()
        print(f" Діапазон температур: {self.temperature_range}", end=" ")
        
class Microwave(KitchenAppliance):
    def __init__(self, brand, power, capacity):
        super().__init__(brand, power)
        self.capacity=capacity
        
    def get_info(self):
        super().get_info()
        print(f" Ємність: {self.capacity}", end=" ")
    

oven_obj=Oven("Bosch", "2,800 watts","50°-270° С")
oven_obj.get_info()
print()
microwave_obj=Microwave("Panasonic", "1,200 watts", "1.2 cubic feet")
microwave_obj.get_info()