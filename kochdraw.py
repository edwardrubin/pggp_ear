from turtle import *

def koch(wid, minwid, sides):
    polygon_ang = 360 / sides
    end_ang = 180 - polygon_ang
    subwid = wid / sides
    armlength = (wid - subwid) / 2
    if (armlength > minwid):
        koch(armlength, minwid, sides)
        left(end_ang)
        for count in range(1, sides):
            koch(subwid, minwid, sides)
            if (count < sides - 1):
                right(polygon_ang)
        left(end_ang)
        koch(armlength, minwid, sides)
    else:
        forward(wid)

def koch_poly(wid, minwid, sides):
    polygon_ang = 360 / sides
    for count in range(sides):
        koch(wid, minwid, sides)
        right(polygon_ang)
    
speed(11)
penup()
backward(300)
left(90)
forward(100)
right(90)
pendown()

koch_poly(300,5,3)
