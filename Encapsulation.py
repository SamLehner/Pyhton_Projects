
# Creating a class classed car
class Car:

    # Setting a private variable __maxspeed to 0
    # Setting a protected variable of name to '' empty for now
    __maxspeed = 0
    _name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self._name = "Supercar"
    
    def drive(self):
        print(str(self._name) + ' driving at maxspeed of ' + str(self.__maxspeed))

    def setMaxSpeed(self,speed):
        self.__maxspeed = speed

        
obj = Car()
obj.drive()
obj.setMaxSpeed(400)
obj.drive()





