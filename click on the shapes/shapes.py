import random
import math
import pygame
from pygame.locals import *
from abc import ABC, abstractmethod

class Shape(ABC):   # this is now an abstract class which means you can't instansitae an object from this class
    def __init__(self, window, shapeType) -> None:
        self.window = window
        self.shapeType = shapeType
        self.color = random.choice(("Red", "White", "Green", "yellow", "Blue"))
        self.x = random.randrange(0, 400)
        self.y = random.randrange(0, 400)
        
    def getType(self):
        return self.shapeType
    
    @abstractmethod
    def clickedInside(self, mousePoint): # this method must be implemented in all the subclasses since it is marked as abstract method
        raise NotImplementedError
    
    @abstractmethod
    def draw(self):
        raise NotImplementedError
    
    def __repr__(self) -> str:
        if self.shapeType == "Triangle" or self.shapeType == "Rectangle":
            return f"{self.shapeType} object {self.width} * {self.height}"
        else:
            return f"Circle object. radius: {self.radius}"


class Rectangle(Shape):
    def __init__(self, window) -> None:
        super().__init__(window, shapeType="Rectangle")
        self.width = random.choice((60, 70, 80, 40, 50))
        self.height = random.choice((60, 70, 80, 40, 50))
        self.area = self.width * self.height
        self.surRect = pygame.Rect(self.x, self.y, self.width, self.height)
        

    def clickedInside(self, mousePos):
        clicked = self.surRect.collidepoint(mousePos)
        return clicked

    # def __eq__(self, otherRect: object) -> bool:
    #     if not isinstance(otherRect, Rectangle):
    #         raise TypeError("Second object is not a rectangle")
    #     if self.area == otherRect.area:
    #         return True
    #     return False

    # def __gt__(self, ohterRect):
    #     if not isinstance(ohterRect, Rectangle):
    #         raise TypeError("Second object is not a rectangle")
    #     if self.area > ohterRect.area:
    #         return True
    #     return False

    # def __lt__(self, ohterRect):
    #     if not isinstance(ohterRect, Rectangle):
    #         raise TypeError("Second object is not a rectangle")
    #     if self.area < ohterRect.area:
    #         return True
    #     return False

    def getArea(self):
        return self.width * self.height

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
    
    # @property    
    # def xyPos(self) -> str:
    #     return f"Postion on window {(self.x, self.y)}"



class Circle(Shape):
    def __init__(self, window):
        super().__init__(window, shapeType="Circle")
        self.radius = random.randrange(10, 50)
        self.centerX = self.x + self.radius
        self.centerY = self.y + self.radius
        self.rect = pygame.Rect(self.x, self.y,
                                            self.radius * 2, self.radius * 2)
        
    def clickedInside(self, mousePoint):
        distance = math.sqrt(((mousePoint[0] - self.centerX) ** 2) +
                                        ((mousePoint[1] - self.centerY) ** 2))
        if distance <= self.radius:
            return True
        else:
            return False

    def getArea(self):
        theArea = math.pi * (self.radius ** 2)
        return theArea

    def draw(self):
        pygame.draw.circle(self.window, self.color,
                                    (self.centerX, self.centerY),
                                    self.radius, 0)
        
class Triangle(Shape):

    def __init__(self, window):
        super().__init__(window, "Triangle")
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.triangleSlope = -1 * (self.height / self.width)
        self.rect = pygame.Rect(self.x, self.y,
                                            self.width, self.height)
        self.shapeType = 'Triangle'
        
    def clickedInside(self, mousePoint):
        inRect = self.rect.collidepoint(mousePoint)
        if not inRect:
            return False

        # Do some math to see if the point is inside the triangle
        xOffset = mousePoint[0] - self.x
        yOffset = mousePoint[1] - self.y
        if xOffset == 0:
            return True

        # Calculate the slope (rise over run)
        pointSlopeFromYIntercept = (yOffset - self.height) / xOffset
        if pointSlopeFromYIntercept < self.triangleSlope:
            return True
        else:
            return False

    def getArea(self):
        theArea = .5 * self.width * self.height
        return theArea

    def draw(self):
        pygame.draw.polygon(self.window, self.color,
            ((self.x, self.y + self.height),
             (self.x, self.y),
             (self.x + self.width, self.y)))