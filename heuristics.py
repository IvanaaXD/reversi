"""canmove(), isLegalMove() and num_valid_moves() are helper functions to *count the
number of valid moves for a given player in a given *board configuration"""

player = "\U000026AB"
computer = "\U000026AA"


"""Assuming my_color stores your color and opp_color stores opponent 's color '-' indicates an empty square on the 
board 'b' indicates a black tile and 'w' indicates a white tile on the board"""


def dynamic_heuristic_evaluation_function(table, color, possitions_player, possitions_computer):
    num_of_color = 0
    num_of_opponent = 0
    i, j, k, my_front_tiles = 0, 0, 0, 0
    opp_front_tiles = 0

    d = 0

    x1 = [-1, -1, 0, 1, 1, 1, 0, -1]
    y1 = [0, 1, 1, 1, 0, -1, -1, -1]

    v = [
        [20, -3, 11, 8, 8, 11, -3, 20],
        [-3, -7, -4, 1, 1, -4, -7, -3],
        [11, -4, 2, 2, 2, 2, -4, 11],
        [8, 1, 2, -3, -3, 2, 1, 8],
        [8, 1, 2, -3, -3, 2, 1, 8],
        [11, -4, 2, 2, 2, 2, -4, 11],
        [-3, -7, -4, 1, 1, -4, -7, -3],
        [20, -3, 11, 8, 8, 11, -3, 20]
    ]

    """v = [[100, -10, 11, 6, 6, 11, -10, 100],
         [-10, -50, 1, 2, 2, 1, -50, -10],
         [10, 1, 5, 4, 4, 5, 1, 10],
         [6, -2, 4, 2, 2, 4, 2, 6],
         [6, -2, 4, 2, 2, 4, 2, 6],
         [10, 1, 5, 4, 4, 5, 1, 10],
         [-10, -50, 1, 2, 2, 1, -50, -10],
         [100, -10, 11, 6, 6, 11, -10, 100]]"""

    """v = [[100, -20, 10, 5, 5, 10, -20, 100],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [5, -2, -1, -1, -1, -1, -2, 5],
    [5, -2, -1, -1, -1, -1, -2, 5],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [100, -20, 10, 5, 5, 10, -20, 100]]"""

    # Piece difference, frontier disks and disk squares

    opponent = player
    if color == player:
        opponent = computer

    for i in range(0, 8):
        for j in range(0, 8):
            if table[i][j] == color:
                d += v[i][j]
                num_of_color += 1
            elif table[i][j] == opponent:
                d -= v[i][j]
                num_of_opponent += 1

            if table[i][j] != "  ":
                for k in range(8):
                    x = i + x1[k]
                    y = j + y1[k]
                    if 0 <= x < 8 and 0 <= y < 8 and table[x][y] == "  ":
                        if table[i][j] == color:
                            my_front_tiles += 1
                        else:
                            opp_front_tiles += 1
                        break

    if num_of_color > num_of_opponent:
        p = (100.0 * num_of_color) / (num_of_color + num_of_opponent)
    elif num_of_color < num_of_opponent:
        p = -(100.0 * num_of_opponent) / (num_of_color + num_of_opponent)
    else:
        p = 0

    if my_front_tiles > opp_front_tiles:
        f = -(100.0 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
    elif my_front_tiles < opp_front_tiles:
        f = (100.0 * opp_front_tiles) / (my_front_tiles + opp_front_tiles)
    else:
        f = 0

    # Corner occupancy
    num_of_color = 0
    num_of_opponent = 0
    if table[0][0] == num_of_color:
        num_of_color += 1
    elif table[0][0] == num_of_opponent:
        num_of_opponent += 1

    if table[0][7] == num_of_color:
        num_of_color += 1
    elif table[0][7] == num_of_opponent:
        num_of_opponent += 1

    if table[7][0] == num_of_color:
        num_of_color += 1
    elif table[7][0] == num_of_opponent:
        num_of_opponent += 1

    if table[7][7] == num_of_color:
        num_of_color += 1
    elif table[7][7] == num_of_opponent:
        num_of_opponent += 1
    c = 25 * (num_of_color - num_of_opponent)

    # Corner closeness
    num_of_color = 0
    num_of_opponent = 0
    if table[0][0] == "  ":
        if table[0][1] == color:
            num_of_color += 1
        elif table[0][1] == opponent:
            num_of_opponent += 1

        if table[1][1] == color:
            num_of_color += 1
        elif table[1][1] == opponent:
            num_of_opponent += 1

        if table[1][0] == color:
            num_of_color += 1
        elif table[1][0] == opponent:
            num_of_opponent += 1

    if table[0][7] == "  ":
        if table[0][6] == color:
            num_of_color += 1
        elif table[0][6] == opponent:
            num_of_opponent += 1

        if table[1][6] == color:
            num_of_color += 1
        elif table[1][6] == opponent:
            num_of_opponent += 1

        if table[1][7] == color:
            num_of_color += 1
        elif table[1][7] == opponent:
            num_of_opponent += 1

    if table[7][0] == "  ":
        if table[7][1] == color:
            num_of_color += 1
        elif table[7][1] == opponent:
            num_of_opponent += 1

        if table[6][1] == color:
            num_of_color += 1
        elif table[6][1] == opponent:
            num_of_opponent += 1

        if table[6][0] == color:
            num_of_color += 1
        elif table[6][0] == opponent:
            num_of_opponent += 1

    if table[7][7] == "  ":
        if table[6][7] == color:
            num_of_color += 1
        elif table[6][7] == opponent:
            num_of_opponent += 1

        if table[6][6] == color:
            num_of_color += 1
        elif table[6][6] == opponent:
            num_of_opponent += 1

        if table[7][6] == color:
            num_of_color += 1
        elif table[7][6] == opponent:
            num_of_opponent += 1

    lll = -12.5 * (num_of_color - num_of_opponent)

    # Mobility

    #opponent = player
    num_of_color = len(possitions_computer)
    num_of_opponent = len(possitions_player)
    if color == player:
        #opponent = computer
        num_of_color = len(possitions_player)
        num_of_opponent = len(possitions_computer)

    if num_of_color > num_of_opponent:
        m = (100.0 * num_of_color) / (num_of_color + num_of_opponent)
    elif num_of_color < num_of_opponent:
        m = -(100.0 * num_of_opponent) / (num_of_color + num_of_opponent)
    else:
        m = 0

    # final weighted score
    score = (10 * p) + (801.724 * c) + (382.026 * lll) + (78.922 * m) + (74.396 * f) + (100 * d)
    return score
