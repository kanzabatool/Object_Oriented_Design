class shape():

    types = ""

    def __init__(self, types=None):
        self.types = types

    def draw(self):
        pass

    def drawline(self):
        pass

    def drawcircle(self):
        pass

class circle(shape):
    def __init__(self, types=None):
        super().__init__()
        self.types = types

    def draw(self):
        print("Drawing the Circle...!")

class rectangle(shape):
    def __init__(self, types=None):
        super().__init__()
        self.types = types

    def draw(self):
        print("Drawing the Rectangle...!")

class drawing(shape):
    def __init__(self, types=None):
        super().__init__()
        self.types = types

    def drawline(self):
        print("This is rectangle diagram")

    def drawcircle(self):
        print("This is circle diagram")

class v1drawing(drawing):
    def __init__(self,):
        super().__init__()
        self.types = "method1"

    def drawline(self):
        print("Method 1 drawing rectangle")

    def drawcircle(self):
        print("Method 1 drawing circle")

class v2drawing(drawing):
    def __init__(self,):
        super().__init__()
        self.types = "method2"

    def drawline(self):
        print("Method 2 drawing rectangle")

    def drawcircle(self):
        print("Method 2 drawing circle")

class DP1(v1drawing):
    def __init__(self):
        super().__init__()
        self.drawline()
        self.drawcircle()

class DP2(v2drawing):
    def __init__(self):
        super().__init__()
        self.drawline()
        self.drawcircle()

if __name__ == '__main__':

    DP = str(input("What design pattern is requested: "))
    if DP == 'DP1':
        DP1()
    else:
        DP2()

