# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    global EMPTY_MARK
    field = [i for i in range(1, 17)]
    for elem in range(len(field)):
        field[elem] = '{0:02d}'.format(field[elem])
    EMPTY_MARK = ' ' + EMPTY_MARK
    field[-1] = EMPTY_MARK
    random.shuffle(field)
    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for element in range(0, len(field), 4):
        print(field[element:element + 4])
    print('\n')


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    if field == ['01', '02', '03', '04',
                 '05', '06', '07', '08',
                 '09', '10', '11', '12',
                 '13', '14', '15', ' x']:
        return True
    else:
        return False


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    index_of_mark = field.index(EMPTY_MARK)
    delta = MOVES[key]
    if (index_of_mark in range(12, 16) and key == 's') \
            or (index_of_mark in range(0, 4) and key == 'w') \
            or (index_of_mark in range(0, 16, 4) and key == 'a') \
            or (index_of_mark in range(3, 16, 4) and key == 'd'):
        raise IndexError('Illegal move!')
    new_index = index_of_mark + delta

    field[index_of_mark], field[new_index] = field[new_index], field[index_of_mark]
    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    message = 'Make your move {}: '.format(', '.join(MOVES.keys()))
    move = input(message)
    while move not in MOVES.keys():
        move = input(message)
    return move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    moves = 0
    field = shuffle_field()
    print_field(field)

    while not is_game_finished(field):
        try:
            move = handle_user_input()
            field = perform_move(field, move)
            moves += 1
            print_field(field)
        except IndexError as ex:
            print(ex)
        except KeyboardInterrupt:
            print('Shutting Down, bye-bye')
            break
    if is_game_finished(field) == True:
        print('CONGRATS! You did in {} moves!'.format(moves))
    else:
        pass


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
