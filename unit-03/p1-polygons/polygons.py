'''
Name: YOUR NAME HERE
P1 Polygons
'''

import turtle


def rect_area(base, height):
    ''' returns the area of a rectangle with given base and height '''
    pass


def circle_area(radius):
    ''' returns the area of a circle with given radius'''
    pass


def triangle_area(base, height):
    ''' returns the area of a triangle with the given base and height'''
    pass


def house_area(base, height):
    ''' returns the area of a house with the given base and height'''
    pass


def draw_rect(turtle_obj, base, height):
    ''' uses turtle_obj to draw a rectangle with the given base and height'''
    pass


def draw_circle(turtle_obj, radius):
    ''' uses turtle_obj to draw a circle with the given radius'''
    pass


def draw_triangle(turtle_obj, side1_len, angle, side2_len):
    ''' uses turtle_obj to draw a triangle with the given side1 length,
    angle and side2 length'''
    pass


def draw_house(turtle_obj, base, height):
    ''' uses turtle_obj to draw a house with the given base and height'''
    pass


def turtle_stuff():
    ''' draws shapes on the screen
    NO NEED TO EDIT THIS FUNCTION'''
    t = turtle.Turtle()
    t.speed(0)

    t.pu()
    t.goto(100, 100)
    t.pd()
    draw_rect(t, 150, 100)

    t.pu()
    t.goto(100, -100)
    t.pd()
    draw_circle(t, 50)

    t.pu()
    t.goto(-100, -100)
    t.pd()
    draw_triangle(t, 100, 90, 100)

    t.pu()
    t.goto(-100, 100)
    t.pd()
    draw_house(t, 150, 100)


def main():
    ''' tests the area functions
    NO NEED TO EDIT THIS FUNCTION'''
    ra = rect_area(4, 3)
    print(ra)                # 12

    ca = circle_area(3)
    print(ca)                # 28.3

    ta = triangle_area(4, 3)  # 6
    print(ta)
    
    ha = house_area(4, 3)     # 16
    print(house_area)

    s = turtle.Screen()
    try:
        turtle_stuff()
    finally:
        s.mainloop()


main()
