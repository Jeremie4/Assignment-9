class Blobber:

    def __init__(self, name, color, radius, height):
        self.name = name
        self.color = color
        self.radius = radius
        self.height = height
        
    def GetName(self):
        return self.name
    
    def GetColor(self):
        return self.color
    
    def GetRadius(self):
        return self.radius
    
    def GetHeight(self):
        return self.height

    def ChangeName(self, name):
        self.name = name
    
    def ChangeColor(self, color):
        self.color = color
    
    def BlobberFeed(self, amount):
        pass

    def vitalsOK(self):
        pass