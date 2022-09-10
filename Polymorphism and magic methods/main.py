import sys
from rect import Rectangle
import pygame
from pygame.locals import *

window_width = 500
window_height = 450
nRects = 10
fps = 30
FIRST_RECT = 'first'
SECOND_RECT = 'second'

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

oRects = []
for _ in range (nRects):
    oRect = Rectangle(window)
    oRects.append(oRect)
whichRect = FIRST_RECT

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for rect in oRects:
                if rect.clickedInside(event.pos):
                    print(f"Clicked on {whichRect} rectangle")

                    if whichRect == FIRST_RECT:
                        oClickedRect1 = rect
                        print(oClickedRect1)
                        whichRect = SECOND_RECT

                    elif whichRect == SECOND_RECT:
                        oClickedRect2 = rect
                        print(oClickedRect2)
                        if oClickedRect1 == oClickedRect2:
                            print(f"Rectangles have the same area {oClickedRect2.getArea()}.")
                        elif oClickedRect1 > oClickedRect2:
                            print(f"First recatangle has area {oClickedRect1.getArea()} > second rectangle {oClickedRect2.getArea()}")
                        elif oClickedRect1 < oClickedRect2:
                            print(f"First recatangle has area {oClickedRect1.getArea()} < second rectangle {oClickedRect2.getArea()}")

                        whichRect = FIRST_RECT

    window.fill(("Black"))
    for rect in oRects:
        rect.draw()
    pygame.display.update()
    clock.tick(fps)