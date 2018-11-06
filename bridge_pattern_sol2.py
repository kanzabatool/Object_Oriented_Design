class shape():

    types = ""

    def __init__(self, types=None):
        self.types = types

    def draw(self):
        pass

class v1shape(shape):
    def __init__(self, types=None):
        super().__init__()
        self.types = types

    def drawline(self):
        print("This is method 1 rectangle diagram")

    def drawcircle(self):
        print("This is method 1 circle diagram")

class v2shape(shape):
    def __init__(self, types=None):
        super().__init__()
        self.types = types

    def drawline(self):
        print("This is method 2 rectangle diagram")

    def drawcircle(self):
        print("This is method 2 circle diagram")

class v1rectangle(v1shape):
    def __init__(self, types=None):
        super().__init__()
        self.types = 'rectangle'

    def draw(self):
        print("Drawing rectangle")


class v1circle(v1shape):
    def __init__(self, types=None):
        super().__init__()
        self.types = 'circle'

    def draw(self):
        print("Drawing circle")

class v2rectangle(v2shape):
    def __init__(self):
        super().__init__()
        self.types = 'rectangle'

    def draw(self):
        print("Drawing rectangle")


class v2circle(v2shape):
    def __init__(self):
        super().__init__()
        self.types = 'circle'

    def draw(self):
        print("Drawing circle")

class DP1(v1shape):
    def __init__(self):
        super().__init__()
        self.drawline()
        self.drawcircle()

class DP2(v2shape):
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

