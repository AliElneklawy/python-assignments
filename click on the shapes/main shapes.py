import sys
from shapes import *
import pygame
from pygame.locals import *

window_width = 500
window_height = 450
nRects = 10
fps = 30
FIRST_SHAPE = 'first'
SECOND_SHAPE = 'second'

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

oShapes = []
classes_dict = {Rectangle:"Rectangle", Circle:"Circle", Triangle:"triangle"}
for _ in range (nRects):
    oClass = random.choice(list(classes_dict))
    oshape = oClass(window)
    oShapes.append(oshape)
_1st_2nd = FIRST_SHAPE

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for shape in oShapes:
                if shape.clickedInside(event.pos):
                    print(f"Clicked on {_1st_2nd} shape")

                    if _1st_2nd == FIRST_SHAPE:
                        oClickedShape1 = shape
                        print(oClickedShape1)
                        _1st_2nd = SECOND_SHAPE

                    elif _1st_2nd == SECOND_SHAPE:
                        oClickedShape2 = shape
                        print(oClickedShape2)
                        # if oClickedShape1 == oClickedShape2:
                        #     print(f"Rectangles have the same area {oClickedShape2.getArea()}.")
                        # elif oClickedShape1 > oClickedShape2:
                        #     print(f"First recatangle has area {oClickedShape1.getArea()} > second rectangle {oClickedShape2.getArea()}")
                        # elif oClickedShape1 < oClickedShape2:
                        #     print(f"First recatangle has area {oClickedShape1.getArea()} < second rectangle {oClickedShape2.getArea()}")

                        _1st_2nd = FIRST_SHAPE

    window.fill((0, 20, 20))
    for shape in oShapes:
        shape.draw()
    pygame.display.update()
    clock.tick(fps)