import time

start_time = time.perf_counter()

class Blobber:

    def __init__(self, name, color, radius, height):
        self.__name = name
        self.__color = color
        self.__radius = radius
        self.__height = height
        self.__start_radius = radius
        
    def GetName(self):
        return str(self.__name).title()
    
    def GetColor(self):
        
        return str(self.__color).lower()

    def ChangeName(self, name):
        self.__name = name
    
    def ChangeColor(self, color):
        self.__color = color
    
    def BlobberFeed(self, amount):
        self.__radius += amount

    def vitalsOK(self):
        vitals = (self.__radius - ((self.__radius * 0.002) * (time.perf_counter() - start_time))) / self.__start_radius

        print(vitals)
        if vitals <= 0.90 or vitals >= 1.10:
            ok = False
        else:
            ok = True

        return vitals, ok

    def Speak(self):
        vitals, ok = self.vitalsOK()
        print("My name is " + str(self.__name).title() + ", and I am " + str(self.__color).lower() + ".\nMy current happiness level is " + format(vitals, ".2%"))
