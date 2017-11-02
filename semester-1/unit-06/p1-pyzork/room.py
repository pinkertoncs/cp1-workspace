'''

Name:

PyZork: room.py

'''


class Room:

    def __init__(self, n, d=""):
        """
        constructor: create a new Room object
        """
        self.name = n
        self.description = d
        self.doors = {}
        self.items = {}


    def __str__(self):
        return self.name

    def connect_to(self, other, direction):
        """
        connect this room to another
        """
        pass

    def add_items(self, items):
        """
        add items to the room
        param: items is a dictionary with
            name / description pairs
        """
        pass

    def print_details(self):
        """
        verbose print for debugging
            prints the room's description
            prints connections & items
        """
        pass


if __name__ == '__main__':

    print('# UNIT TESTS FOR ROOM')
