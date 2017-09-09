'''
Name: YOUR NAME HERE
P1 Polygons
'''

import turtle


def rect_area(b, h):
    pass


def circle_area(r):
    pass


def triangle_area(b, h):
    pass


def house_area(b, h):
    pass


def draw_rect(t, b, h):
    pass


def draw_circle(t, r):
    pass


def draw_triangle(t, s1, a, s2):
    pass


def draw_house(t, b, h):
    pass


def turtle_stuff():
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
    ra = rect_area(4, 3)
    print(ra)                # 12

    ca = circle_area(3)
    print(ca)                # 28.3

    ta = triangle_area(4, 3)  # 6
    print(ta)
    
    ha = house_area(4, 3)     # 16
    print(ha)

    s = turtle.Screen()
    try:
        turtle_stuff()
    finally:
        s.mainloop()


main()
