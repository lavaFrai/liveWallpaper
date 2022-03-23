class Color:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def get(self):
        return self.red, self.green, self.blue
