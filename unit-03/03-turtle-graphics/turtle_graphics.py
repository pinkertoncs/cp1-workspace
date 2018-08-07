'''

Practice: Turtle graphics

see README.md for notes

'''

import turtle


def turtle_stuff():

    # create a turtle
    joe = turtle.Turtle()

    #
    # YOUR CODE HERE
    #

    # Use variable joe to
    #
    # - Draw a straight line
    # - Draw a path with multiple turns (try to write out you name)
    # - Draw a curve / circle
    # - Use multiple colors
    # - Use multiple pen widths
    #

    # Show how to
    # - Pick the pen up / put the pen down
    # - Get / Set the position of a turtle
    # - Get / Set the heading of a turtle

    # Use print statements to answer the following questions
    # - What is the difference between a class and an object?
    # - Name 3 attributes os a Turtle
    # - Name 3 methods of a Turtle


def main():

    s = turtle.Screen()
    try:
        turtle_stuff()
    finally:
        s.mainloop()


if __name__ == '__main__':
    main()
