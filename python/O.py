class car:
    
    def __init__(self,s,y):
        self.speed = s     ###self.speed and self.year are the attributes 
        self.year=y
    def get_speed(self):                                      ##def get_speed and the def setspeed are the methods
        print("Max speed is" ,self.speed)
    def setspeed(self,s):
        self.speed=s
        
BMW=car(180,2023)
Ford=car(234,2045)

BMW.get_speed()
BMW.setspeed(120)        #Encapsulation is used for data hiding and miss modification,original data remains safe
BMW.get_speed()


class sedan(car):
    def accelerate(self):    #child class
        print('132')
class SUV(car):  ##child class
    def accelerate(self):
        print('145')

Honda=sedan(180,2013)
Toyota=SUV(202,2034)
Honda.get_speed
Honda.accelerate()  #Inheritance is used to inherit the properties of parent class to child class