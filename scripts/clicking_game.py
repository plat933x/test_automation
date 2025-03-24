import pygame as py

size = (500,400)
screen = py.display.set_mode(size)

while True:
    for ev in py.event.get():
        if ev.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            col = (100, 215, 65)
            py.draw.circle(
            screen, col, pos, 20, 5
            )
            py.display.update()