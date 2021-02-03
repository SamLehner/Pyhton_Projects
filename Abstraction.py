

from abc import ABC, abstractmethod



class Taxi(ABC):
    def rideCost(self,amount):
        print("The cost of your ride today is: ",amount)
    # This function is telling us to pass in an argument, but we wont tell you
    # how or what kind of data it will be
    @abstractmethod
    def cost(self,amount):
        pass

class CreditCardCost(Taxi):
    # Here we define how to implement the payment function from its parent class cost
    def cost(self,amount):
        print('Your ride cost of {} exceeded your 150$ limit'.format(amount))


obj = CreditCardCost()
obj.rideCost("300$")
obj.cost("300$")
