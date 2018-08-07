
class Person:

    # 2. Add a parameter a=0 to the constructor
    # 3. Assign the calling object's age to the parameter
    #   a in the constructor
    def __init__(self, n="Anonymous"):
        """
        constructor
        """
        self.name = n
        self.hobbies = []

    def __str__(self):
        """
        string casting method
        """
        return self.name

    # 4. Modify this function so that it prints the
    #   Person's age after name
    def say_hello(self):
        print("Hi, my name is", self.name)

        if self.hobbies:
            print("I like", end=' ')
            for hobby in self.hobbies:
                print(hobby, end=', ')
            print()

    def add_hobby(self, h):
        self.hobbies.append(h)

    # 8. implement a method add_hobbies that takes
    #   a list of hobbies and adds all of them
    #   to the object's hobbies list


def main():

    # 1. Use print statements to compare and contrast
    #   a. class and objects
    #   b. attribute and methods

    joe = Person("Joe")
    joe.add_hobby("skiing")
    joe.add_hobby("trains")
    joe.add_hobby("turtles")
    joe.say_hello()
    print('---')
    sam = Person('Sam')
    sam.say_hello()

    # 5. Create three Person objects: one with no arguments,
    #   one with name, and one with name and age

    # 6. Call say_hello for each of the three objects

    # 7. add some hobbies to a person. Call say_hello

    # 9. Use print statements to compare and contrast
    #   a. functional programming & object-oriented programming
    #   b. function composition & object composition


main()
