'''

Name:

P1 Loops

'''

# imports
import turtle


def print_mult_table(n):
    pass


def print_chess(rows, columns):
    pass


def draw_poly(t, n, s):
    pass


def draw_coords(t, points):
    pass


def draw_chess(t, rows, cols, s):
    pass


def draw_star(t, n, w):
    pass


def test_collections():
    print('\n# printMultTable')
    print_mult_table(5)

    print('\n# printChess')
    print_chess(3, 3)


def test_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)

    draw_chess(t, 5, 5, 50)

    t.color('blue')
    t.pu()
    t.goto(-200, 200)
    t.pd()
    draw_poly(t, 5, 100)

    t.color('green')
    coords = [(100, 200), (300, 100), (0, 150)]
    draw_coords(t, coords)

    t.pu()
    t.goto(-300, -100)
    t.pd()
    t.color('red')
    draw_star(t, 5, 100)


def main():
    test_collections()
    wn = turtle.Screen()
    try:
        test_turtle()
    finally:
        wn.mainloop()


if __name__ == "__main__":
    main()
