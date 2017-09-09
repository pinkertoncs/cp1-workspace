import room
import player


class Game:

    def __init__(self):    
        """
         constructor: create a Game object
        initialize your game in here
        """    
        self.rooms = []
        self.player = player.Player()
        pass

    def print_rooms(self):
        """
        print function for debugging
        calls print for all rooms
        """
        pass

    def process_cmd(self, cmd, args):
        """
        process given command
        params is a list of arguments
        """
        pass

    def start(self):
        """
        start the input loop:
            1. get user input (command)
            2. split into tokens
            3. process the command
        """
        pass


if __name__ == '__main__':
    g = Game()
    g.start()
