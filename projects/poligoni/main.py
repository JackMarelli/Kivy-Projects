import math

from kivy.lang import Builder
from kivy.uix.accordion import Accordion
from kivy.app import App

Builder.load_file("all.kv")

class Polygon():

    type = ""           #what poligon
    side = 0            #used in square
    shortSide = 0       #used in trapezium
    longSide = 0        #used in trapezium
    base = 0            #used in rect and triangle
    height = 0          #used in rect and triangle

    area = 0            #area of polygon
    perimeter = 0       #perimeter of polygon

    def __init__(self, type = "", side = 0, shortSide = 0, longSide = 0, base = 0, height = 0):
        self.type = type
        self.side = side
        self.shortSide = shortSide
        self.longSide = longSide
        self.base = base
        self.height = height

        if self.type == "square":
            self.area = self.side ** 2
            self.perimeter = self.side * 4
        elif self.type == "triangle_e":
            self.area = math.sqrt(3) / 4 * (side ** 2) #check math
            self.perimeter = self.side * 3
        elif self.type == "rectangle":
            self.area = self.base * self.height
            self.perimeter = self.base * 2 + self.height * 2
        else:
            return None

class Accord(Accordion):

    def getResults(self, polygonType):
        if polygonType == "square":
            p = Polygon(type = polygonType, side = int(self.ids["txtSquareSide"].text))
        elif polygonType == "triangle_e":
            p = Polygon(type = polygonType, side = int(self.ids["txtTriangleSide"].text))
        elif polygonType == "rectangle":
            p = Polygon(type = polygonType, base = int(self.ids["txtRectangleBase"].text), height = int(self.ids["txtRectangleHeight"].text))

        print(p.area)
        print(p.perimeter)

class AccordionApp(App):

    def build(self):
        return Accord()

if __name__ == '__main__':
    AccordionApp().run()