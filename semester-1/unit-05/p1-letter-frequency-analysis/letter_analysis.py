"""

Name:

P1 - Letter Frequency analysis

"""

import matplotlib.pyplot as plt

# Dictionary that holds a letter -> count
letters_freq = {}


def read_file(filename):
    """
    loops through filename and passes each
    line to parse sentence
    """
    pass


def parse_sentence(line):
    """
    loops through line and passes each
    word to analyze_word
    """
    pass


def analyze_word(word):
    """
    Reads each letter of word, if it is a letter a-z
    increment that letter frequency by 1

    Q: Should case (upper/lower) matter?
    Q: How do know if a character is a letter?
    """
    pass


def preprocess_data():
    """
    returns a tuple of a list of labels and a list of data
    from letters_freq

    e.g. if letters_freq = {'a': 2, 'z': 3, 'f': 23}
    then this function returns (['a', 'f', 'z'], [2, 23, 3])
    """
    pass


def make_graph():
    """
    Which format would work best for graphic letters_freq (pie, bar, line, other?)

    graph letters_freq in a format of your choosing
    """
    pass


def main():

    read_file("test-input.txt")
    make_graph()

    # read a second text file and graph it's letter frequency


if __name__ == '__main__':
    main()
