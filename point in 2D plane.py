from math import sqrt

class Point():
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0, 0)
        
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    
    def xMove(self, newX):
        self.x = newX
        
    def yMove(self, newY):
        self.y = newY
        
    @property    
    def mag(self):
        return sqrt((self.x)**2 + (self.y)**2)
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
 

from random import randint
points1 = []
points2 = []
for i in range(5):
    p1 = Point(randint(-10, 10), randint(-10, 10))
    points1.append(p1)
    p2 = Point(randint(-5, 5), randint(-5, 5))
    points2.append(p2)
print(points1)
