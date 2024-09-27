from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name, model, power_level=0):
        self.name=name
        self.model=model
        self.power_level=power_level
    
    @abstractmethod
    def perform_task(self):
        pass

    def show_info(self):
        print(f"Name {self.name}, model {self.model}, power level {self.power_level}")

    def charge(self, charge):
        self.charge=charge
        if charge <=100:
            print(f"Старий заряд: {self.power_level}")
            self.power_level+=charge
            print(f"Новий заряд: {self.power_level}")
        else:
            print('Максимальна кількість збільлення - 100')
        
class WorkerRobot(Robot):
    def __init__(self, name, model, power_level, tool):
        super().__init__(name, model, power_level)
        self.tool=tool
        
    def perform_task(self):
        if self.power_level>=10:
            self.power_level-=10
            print(f"Завдання виконується з інструментом {self.tool}. Заряд: {self.power_level}")
        else:
            print("У вас недостатньо заряду")


class DefenseRobot(Robot):
    def __init__(self, name, model, power_level, weapon):
        super().__init__(name, model, power_level)
        self.weapon=weapon
        
    def perform_task(self):
        if self.power_level>=15:
            self.power_level-=15
            print(f"Захисне завдання виконується зі зброєю {self.weapon}. Заряд: {self.power_level}")
        else:
            print("У вас недостатньо заряду")

class ServiceRobot(Robot):
    def __init__(self, name, model, power_level, service_type):
        super().__init__(name, model, power_level)
        self.service_type=service_type

    def perform_task(self):
        if self.power_level>=5:
            self.power_level-=5
            print(f"Надається послуга: {self.service_type}. Заряд: {self.power_level}")
        else:
            print("У вас недостатньо заряду")


obj1=WorkerRobot("Bob", "X1", 10, "wrench")
obj1.charge(20)
obj1.show_info()
obj1.perform_task()
print()
obj2=DefenseRobot("Defender", "Z3", 20, "laser")
obj2.charge(30)
obj2.show_info()
obj2.perform_task()
print()
obj3=ServiceRobot("Helper", "S2", 25, "cleaning")
obj3.charge(15)
obj3.show_info()
obj3.perform_task()