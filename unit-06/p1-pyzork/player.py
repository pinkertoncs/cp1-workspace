import room


class Player:

    def __init__(self, location=None, items={}):
        """
        new Player constructor
            location and items are OPTIONAL parameters
            The values in the param list are DEFAULT values
        """
        self.location = location
        self.items = items

    def __str__(self):
        """
        get string representation of Player
        """
        return ''

    def goto(self, rm):
        """
        go to a room
        """
        pass

    def go(self, direction):
        """
        go in a direction
        """
        pass

    def look(self, item=None):
        """
        look around, or look at an item
        """
        pass

    def take(self, item):
        """
        take an item
        """
        pass


if __name__ == '__main__':

    print('# UNIT TESTS FOR PLAYER')
