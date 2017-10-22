from os import system


def clear():
    """
    Using import os to access the system command called cls, this will clear the window after each while iteration.
    :return: OS Command 'cls'
    """
    system('clear')


def top():
    """
    The top section of the playing board including the Column number and top line
    :return: Static top row; 1 to 3 and the horizontal line.
    """
    return "    1   2   3 \n" \
           "  " + "+---" * 3 + "+"


def bottom():
    """
    The Bottom section of the playing board including the bottom line
    :return: Static top row with the horizontal line.
    """
    return "  " + "+---" * 3 + "+"


def play_area(board):
    """
    This function will printout the line based on the line letter
    :param board: Line identifier: A, B, or C
    :return: Line identifier from the param and the bottom closing horizontal line of the cell
    """
    # Setting initial variables that will be use during
    a1 = " "
    a2 = " "
    a3 = " "
    b1 = " "
    b2 = " "
    b3 = " "
    c1 = " "
    c2 = " "
    c3 = " "

    board.sort()

    for selection in board:
        rnd = selection.split('.')
        plr = rnd[0]
        rnd_selec = rnd[1].lower()

        # Lets draw the top row
        if rnd_selec[0] == 'a' and rnd_selec[1] == '1':
            a1 = plr
        elif rnd_selec[0] == 'a' and rnd_selec[1] == '2':
            a2 = plr
        elif rnd_selec[0] == 'a' and rnd_selec[1] == '3':
            a3 = plr

        # Lets draw the second row
        elif rnd_selec[0] == 'b' and rnd_selec[1] == '1':
            b1 = plr
        elif rnd_selec[0] == 'b' and rnd_selec[1] == '2':
            b2 = plr
        elif rnd_selec[0] == 'b' and rnd_selec[1] == '3':
            b3 = plr

        # Lets draw the third row
        elif rnd_selec[0] == 'c' and rnd_selec[1] == '1':
            c1 = plr
        elif rnd_selec[0] == 'c' and rnd_selec[1] == '2':
            c2 = plr
        elif rnd_selec[0] == 'c' and rnd_selec[1] == '3':
            c3 = plr

    return \
        "A " + "| " + a1 + " | " + a2 + " | " + a3 + " |\n" \
        "  " + "+---" * 3 + "+\n" \
        "B " + "| " + b1 + " | " + b2 + " | " + b3 + " |\n" \
        "  " + "+---" * 3 + "+\n" \
        "c " + "| " + c1 + " | " + c2 + " | " + c3 + " |"


def count(selections):
    """
    Determine if there is a winner
    :param selections: The list with the players selections on the board
    :return: Will return a winner of a player gets three selections in a row, column, or diagonally.
    """

    player_X = [selection for selection in selections if selection[0] == 'X']
    player_X_a = [selection for selection in player_X if selection[-2] == 'a']
    player_X_b = [selection for selection in player_X if selection[-2] == 'b']
    player_X_c = [selection for selection in player_X if selection[-2] == 'c']
    player_X_1 = [selection for selection in player_X if selection[-1] == '1']
    player_X_2 = [selection for selection in player_X if selection[-1] == '2']
    player_X_3 = [selection for selection in player_X if selection[-1] == '3']

    player_X_db = [selection for selection in player_X if
                   (selection[-2] == 'a' and selection[-1] == '1') or
                   (selection[-2] == 'b' and selection[-1] == '2') or
                   (selection[-2] == 'c' and selection[-1] == '3')
                   ]

    player_X_df = [selection for selection in player_X if
                   (selection[-2] == 'a' and selection[-1] == '3') or
                   (selection[-2] == 'b' and selection[-1] == '2') or
                   (selection[-2] == 'c' and selection[-1] == '1')
                   ]

    player_O = [selection for selection in selections if selection[0] == 'O']
    player_O_a = [selection for selection in player_O if selection[-2] == 'a']
    player_O_b = [selection for selection in player_O if selection[-2] == 'b']
    player_O_c = [selection for selection in player_O if selection[-2] == 'c']
    player_O_1 = [selection for selection in player_O if selection[-1] == '1']
    player_O_2 = [selection for selection in player_O if selection[-1] == '2']
    player_O_3 = [selection for selection in player_O if selection[-1] == '3']

    player_O_db = [selection for selection in player_O if
                   (selection[-2] == 'a' and selection[-1] == '1') or
                   (selection[-2] == 'b' and selection[-1] == '2') or
                   (selection[-2] == 'c' and selection[-1] == '3')
                   ]

    player_O_df = [selection for selection in player_O if
                   (selection[-2] == 'a' and selection[-1] == '3') or
                   (selection[-2] == 'b' and selection[-1] == '2') or
                   (selection[-2] == 'c' and selection[-1] == '1')
                   ]

    if len(player_X_a) == 3:
        return "Player X won!"
    elif len(player_O_a) == 3:
        return "Player O won!"

    if len(player_X_b) == 3:
        return "Player X won!"
    elif len(player_O_b) == 3:
        return "Player O won!"

    if len(player_X_c) == 3:
        return "Player X won!"
    elif len(player_O_c) == 3:
        return "Player O won!"

    if len(player_X_1) == 3:
        return "Player X won!"
    elif len(player_O_1) == 3:
        return "Player O won!"

    if len(player_X_2) == 3:
        return "Player X won!"
    elif len(player_O_2) == 3:
        return "Player O won!"

    if len(player_X_3) == 3:
        return "Player X won!"
    elif len(player_O_3) == 3:
        return "Player O won!"

    if len(player_X_db) == 3:
        return "Player X won!"
    elif len(player_O_db) == 3:
        return "Player O won!"

    if len(player_X_df) == 3:
        return "Player X won!"
    elif len(player_O_df) == 3:
        return "Player O won!"
    pass


board_selections = []
player = ''
while True:

    clear()
    print(top())
    print(play_area(board_selections))
    print(bottom())

    if player != 'X':
        player = 'X'
    else:
        player = 'O'

    player_selection = input("Player %s, please make your selection, example a3 or c2 etc:" % player)
    while True:
        if [board_selection.split('.')[1] for board_selection in board_selections if player_selection in board_selection]:
            player_selection = input("The board was already selected, please select a valid block:")
        else:
            break

    board_selections.append(player + '.' + player_selection)

    if count(board_selections) != None:
        clear()
        print(count(board_selections))
        print(top())
        print(play_area(board_selections))
        print(bottom())
        break
