import random
import pygame

class Rectangle():
    def __init__(self, window) -> None:
        self.window = window
        self.__width = random.choice((60, 70, 80, 40, 50))
        self.__height = random.choice((60, 70, 80, 40, 50))
        self.__area = self.__width * self.__height
        self.color = random.choice(("Red", "White", "Green", "yellow", "Blue"))
        self.__x = random.randrange(0, 400)
        self.__y = random.randrange(0, 400)
        self.surRect = pygame.Rect(self.__x, self.__y, self.__width, self.__height)

    def clickedInside(self, mousePos):
        clicked = self.surRect.collidepoint(mousePos)
        return clicked

    def __eq__(self, otherRect: object) -> bool:
        if not isinstance(otherRect, Rectangle):
            raise TypeError("Second object is not a rectangle")
        if self.__area == otherRect.__area:
            return True
        return False

    def __gt__(self, ohterRect):
        if not isinstance(ohterRect, Rectangle):
            raise TypeError("Second object is not a rectangle")
        if self.__area > ohterRect.__area:
            return True
        return False

    def __lt__(self, ohterRect):
        if not isinstance(ohterRect, Rectangle):
            raise TypeError("Second object is not a rectangle")
        if self.__area < ohterRect.__area:
            return True
        return False

    def getArea(self):
        return self.__width * self.__height

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.__x, self.__y, self.__width, self.__height))
    
    @property    
    def xyPos(self) -> str:
        return f"Postion on window {(self.__x, self.__y)}"
        
    def __repr__(self) -> str:
        return f"Rectangle object {self.__width} * {self.__height}"
