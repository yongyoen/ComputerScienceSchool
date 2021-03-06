#abstract class
from abc import *

class Person(metaclass = ABCMeta):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        
    @abstractmethod
    def transaction(self, other, how_many):
        pass

    def giveMoney(self, other,how_much):
        if how_much <=self.money:
            other.money +=how_much
            self.money -= how_much
        else:
            print("you don't have {0}".format(how_much))



            
