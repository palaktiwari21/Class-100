class Car :
    def __init__(self,modle,colour,company,speed_limit):
        self.colour=colour
        self.company=company
        self.speed_limit=speed_limit
        self.modle=modle
    def start():
        print("car is starting")

    def stop():
        print("car has stopped")

    def change_gear():
        print("car has changed its gear")



audi=Car("audiA5","black","Audi","180")

#print(audi.colour)
Car.stop()