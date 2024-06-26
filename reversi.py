import copy
import math
import time

from heuristics import dynamic_heuristic_evaluation_function

player = "\U000026AB"
computer = "\U000026AA"

table = [["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", computer, player, "  ", "  ", "  "],
         ["  ", "  ", "  ", player, computer, "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]]

heuristike = {}


def print_table(table):
    print("     A    B    C    D    E    F    G    H  ")
    print("1:  " + table[0][0] + " | " + table[0][1] + " | " + table[0][2] + " | " + table[0][3] + " | " + table[0][
        4] + " | " + table[0][5] + " | " + table[0][6] + " | " + table[0][7])
    print("   ----------------------------------------")
    print("2:  " + table[1][0] + " | " + table[1][1] + " | " + table[1][2] + " | " + table[1][3] + " | " + table[1][
        4] + " | " + table[1][5] + " | " + table[1][6] + " | " + table[1][7])
    print("   ----------------------------------------")
    print("3:  " + table[2][0] + " | " + table[2][1] + " | " + table[2][2] + " | " + table[2][3] + " | " + table[2][
        4] + " | " + table[2][5] + " | " + table[2][6] + " | " + table[2][7])
    print("   ----------------------------------------")
    print("4:  " + table[3][0] + " | " + table[3][1] + " | " + table[3][2] + " | " + table[3][3] + " | " + table[3][
        4] + " | " + table[3][5] + " | " + table[3][6] + " | " + table[3][7])
    print("   ----------------------------------------")
    print("5:  " + table[4][0] + " | " + table[4][1] + " | " + table[4][2] + " | " + table[4][3] + " | " + table[4][
        4] + " | " + table[4][5] + " | " + table[4][6] + " | " + table[4][7])
    print("   ----------------------------------------")
    print("6:  " + table[5][0] + " | " + table[5][1] + " | " + table[5][2] + " | " + table[5][3] + " | " + table[5][
        4] + " | " + table[5][5] + " | " + table[5][6] + " | " + table[5][7])
    print("   ----------------------------------------")
    print("7:  " + table[6][0] + " | " + table[6][1] + " | " + table[6][2] + " | " + table[6][3] + " | " + table[6][
        4] + " | " + table[6][5] + " | " + table[6][6] + " | " + table[6][7])
    print("   ----------------------------------------")
    print("8:  " + table[7][0] + " | " + table[7][1] + " | " + table[7][2] + " | " + table[7][3] + " | " + table[7][
        4] + " | " + table[7][5] + " | " + table[7][6] + " | " + table[7][7])
    print("")


def space_is_free(tabla, position):
    list = []

    for part in position:
        list.append(part)

    slovo = ord(list[0]) - 65
    broj = int(list[1]) - 1
    if tabla[broj][slovo] == "  ":
        return True
    return False


def possible_positions(tabla, color):
    dict = {}

    opponent = player
    if color == player:
        opponent = computer

    for i in range(8):
        for j in range(8):
            if tabla[i][j] == color:
                br_i = i
                br_j = j

                # horizontalno udesno
                h = 0
                list_hud = []
                for k in range(br_j + 1, 8):
                    if tabla[i][k] == opponent:
                        h += 1
                        reverse = chr(k + 65) + str(i + 1)
                        list_hud.append(reverse)
                        continue
                    elif tabla[i][k] == color:
                        break
                    else:
                        if h == 0:
                            break
                        else:
                            possible_p = chr(k + 65) + str(i + 1)
                            if space_is_free(tabla, possible_p):

                                if possible_p in dict.keys():
                                    dict[possible_p].extend(list_hud)
                                else:
                                    dict[possible_p] = list_hud
                            break

                # horizontalno ulijevo
                h = 0
                list_hul = []
                for k in range(br_j - 1, -1, -1):
                    if tabla[i][k] == opponent:
                        h += 1
                        reverse = chr(k + 65) + str(i + 1)
                        list_hul.append(reverse)
                        continue
                    elif tabla[i][k] == color:
                        break
                    else:
                        if h == 0:
                            break
                        else:
                            possible_p = chr(k + 65) + str(i + 1)
                            if space_is_free(tabla, possible_p):

                                if possible_p in dict:
                                    dict[possible_p].extend(list_hul)

                                else:
                                    dict[possible_p] = list_hul

                                break

                # vertikalno dolje
                v = 0
                list_vd = []
                for k in range(br_i + 1, 8):
                    if tabla[k][j] == opponent:
                        v += 1
                        reverse = chr(j + 65) + str(k + 1)
                        list_vd.append(reverse)
                        continue
                    elif tabla[k][j] == color:
                        break
                    else:
                        if v == 0:
                            break
                        else:
                            possible_p = chr(j + 65) + str(k + 1)
                            if space_is_free(tabla, possible_p):

                                if possible_p in dict.keys():
                                    dict[possible_p].extend(list_vd)
                                else:
                                    dict[possible_p] = list_vd

                                break

                # vertikalno gore
                v = 0
                list_vg = []
                for k in range(br_i - 1, -1, -1):
                    if tabla[k][j] == opponent:
                        v += 1
                        reverse = chr(j + 65) + str(k + 1)
                        list_vg.append(reverse)
                        continue
                    elif tabla[k][j] == color:
                        break
                    else:
                        if v == 0:
                            break
                        else:
                            possible_p = chr(j + 65) + str(k + 1)
                            if space_is_free(tabla, possible_p):

                                if possible_p in dict.keys():
                                    dict[possible_p].extend(list_vg)
                                else:
                                    dict[possible_p] = list_vg

                            break

                # dijagonalno lijevo gore
                d = 0
                list_dlg = []
                br_i = i - 1
                br_j = j
                kraj = 1
                for k in range(br_i, -1, -1):
                    br_j -= 1
                    for p in range(br_j, -1, -1):
                        if tabla[k][p] == opponent:
                            d += 1
                            reverse = chr(p + 65) + str(k + 1)
                            list_dlg.append(reverse)
                        elif tabla[k][p] == color:
                            d = 0
                            kraj = 0
                            break
                        else:
                            if d == 0:
                                kraj = 0
                                break
                            elif tabla[k + 1][p + 1] == "  ":
                                kraj = 0
                                break
                            else:
                                possible_p = chr(p + 65) + str(k + 1)

                                if space_is_free(tabla, possible_p):

                                    if possible_p in dict.keys():
                                        dict[possible_p].extend(list_dlg)
                                        d -= len(list_dlg)
                                        kraj = 0
                                    else:
                                        dict[possible_p] = list_dlg
                                        d -= len(list_dlg)
                                        kraj = 0
                                        break
                        break

                    if kraj != 0:
                        continue
                    else:
                        break

                # dijagonalno desno gore
                d = 0
                list_ddg = []
                br_j = j
                br_i = i - 1
                kraj = 1
                for k in range(br_i, -1, -1):
                    br_j += 1
                    for p in range(br_j, 8):
                        if tabla[k][p] == opponent:
                            d += 1
                            reverse = chr(p + 65) + str(k + 1)
                            list_ddg.append(reverse)
                        elif tabla[k][p] == color:
                            d = 0
                            kraj = 0
                            break
                        else:
                            if d == 0:
                                kraj = 0
                                break
                            elif tabla[k + 1][p - 1] == "  ":
                                kraj = 0
                                break
                            else:
                                possible_p = chr(p + 65) + str(k + 1)
                                if space_is_free(tabla, possible_p):

                                    if possible_p in dict.keys():
                                        dict[possible_p].extend(list_ddg)
                                        d -= len(list_ddg)
                                        kraj = 0
                                    else:
                                        dict[possible_p] = list_ddg
                                        d -= len(list_ddg)
                                        kraj = 0
                                        break
                        break
                    if kraj != 0:
                        continue
                    else:
                        break

                # dijagonalno lijevo dolje
                d = 0
                list_dld = []
                br_j = j
                br_i = i + 1
                kraj = 1
                for k in range(br_i, 8):
                    br_j -= 1
                    for p in range(br_j, -1, -1):
                        if tabla[k][p] == opponent:
                            d += 1
                            reverse = chr(p + 65) + str(k + 1)
                            list_dld.append(reverse)
                        elif tabla[k][p] == color:
                            d = 0
                            kraj = 0
                            break
                        else:
                            if d == 0:
                                kraj = 0
                                break
                            elif tabla[k - 1][p + 1] == "  ":
                                kraj = 0
                                break
                            else:
                                possible_p = chr(p + 65) + str(k + 1)
                                if space_is_free(tabla, possible_p):

                                    if possible_p in dict.keys():
                                        dict[possible_p].extend(list_dld)
                                        d -= len(list_dld)
                                        kraj = 0
                                    else:
                                        dict[possible_p] = list_dld
                                        d -= len(list_dld)
                                        kraj = 0
                                        break
                        break

                    if kraj != 0:
                        continue
                    else:
                        break

                # dijagonalno desno dolje
                d = 0
                list_ddd = []
                br_j = j
                br_i = i + 1
                kraj = 1
                for k in range(br_i, 8):
                    br_j += 1
                    for p in range(br_j, 8):
                        if tabla[k][p] == opponent:
                            d += 1
                            reverse = chr(p + 65) + str(k + 1)
                            list_ddd.append(reverse)
                        elif tabla[k][p] == color:
                            d = 0
                            kraj = 0
                            break
                        else:
                            if d == 0:
                                kraj = 0
                                break
                            elif tabla[k - 1][p - 1] == "  ":
                                kraj = 0
                                break
                            else:
                                possible_p = chr(p + 65) + str(k + 1)
                                if space_is_free(tabla, possible_p):

                                    if possible_p in dict.keys():
                                        dict[possible_p].extend(list_ddd)
                                        d -= len(list_ddd)
                                        kraj = 0
                                    else:
                                        dict[possible_p] = list_ddd
                                        d -= len(list_ddd)
                                        kraj = 0
                                        break
                        break

                    if kraj != 0:
                        continue
                    else:
                        break

    return dict


def insert(color, position, dictionary):
    brojac = 0
    for key in dictionary.keys():

        if position == key:

            brojac += 1

            list = []
            for part in position:
                list.append(part)

            slovo = ord(list[0]) - 65
            broj = int(list[1]) - 1

            table[broj][slovo] = color

    if brojac == 0:
        print("Invalid position!")
        position = input("Please enter a new position: ").upper()
        insert(color, position, dictionary)
        return

    values = []
    for value in dictionary[position]:
        values.append(value)

    for key in dictionary.keys():
        for value in dictionary[key]:
            for v in values:
                if v == value:

                    list = []
                    for part in value:
                        list.append(part)

                    slovo = ord(list[0]) - 65
                    broj = int(list[1]) - 1

                    table[broj][slovo] = color

    print_table(table)
    return


def possible_insert(color, position, lista, copy_of_table):
    list = []
    for part in position:
        list.append(part)

    slovo = ord(list[0]) - 65
    broj = int(list[1]) - 1

    copy_of_table[broj][slovo] = color

    for value in lista:

        for part in value:
            list.append(part)

        slovo = ord(list[0]) - 65
        broj = int(list[1]) - 1

        copy_of_table[broj][slovo] = color

    return copy_of_table


def game_over(table):
    brojac = 0
    for i in range(8):
        for j in range(8):
            if table[i][j] != computer and table[i][j] != player:
                brojac += 1
                break

    if brojac > 0:
        return False
    else:
        return True


def count():
    num_of_white = 0
    num_of_black = 0
    for i in range(8):
        for j in range(8):
            if table[i][j] == computer:
                num_of_white += 1
            elif table[i][j] == player:
                num_of_black += 1
            else:
                continue

    print("Player: ", num_of_black)
    print("Computer: ", num_of_white)


def check_who_won():
    num_of_white = 0
    num_of_black = 0
    for i in range(8):
        for j in range(8):
            if table[i][j] == computer:
                num_of_white += 1
            elif table[i][j] == player:
                num_of_black += 1
            else:
                continue

    if num_of_black > num_of_white:
        print("Player wins!")
    elif num_of_white > num_of_black:
        print("Computer wins!")
    else:
        print("Draw!")

    print("Player won: ", num_of_black, "and computer won: ", num_of_white, "points.")
    exit()


def player1_move():
    positions = possible_positions(table, player)
    if len(positions) == 0:
        over(player)
    print("Possible positions are: ")

    for position in positions.keys():
        print(position, ", changes: ", positions[position])
    position = input("Enter a position: ").upper()
    insert(player, position, positions)
    return


def player2_move():
    positions = possible_positions(table, computer)
    if len(positions) == 0:
        over(computer)
    print("Possible positions are: ", positions)
    position = input("Enter a position: ").upper()
    insert(computer, position, positions)
    return


def computer_move():
    best_score = -math.inf
    best_move = None

    positions = possible_positions(table, computer)

    if len(positions) >= 7:
        depth = 5
    else:
        depth = 6

    if len(positions) == 0:
        over(computer)

    for position in positions.keys():
        list = []

        for part in position:
            list.append(part)

        slovo = ord(list[0]) - 65
        broj = int(list[1]) - 1

        if table[broj][slovo] == "  ":
            tabla = copy.deepcopy(table)
            tabla[broj][slovo] = computer
            vrijeme = time.time()
            score = minimax_alpha_beta(copy.deepcopy(tabla), depth, -math.inf, math.inf, True, vrijeme)
            if score > best_score:
                best_score = score
                best_move = chr(slovo + 65) + str(broj + 1)

    insert(computer, best_move, positions)


def minimax_alpha_beta(tabla, depth, alpha, beta, maximizing_player, vrijeme):
    global heuristike

    if depth == 0 or is_terminal_node(tabla) or time.time() - vrijeme <= 3.7:

        if str(tabla) in heuristike:
            return heuristike[str(tabla)]
        else:
            heuristika = dynamic_heuristic_evaluation_function(tabla, computer, possible_positions(tabla, player), possible_positions(tabla, computer))
            heuristike[str(tabla)] = heuristika
            return heuristika

    if maximizing_player:
        max_eval = -math.inf
        positions = possible_positions(tabla, computer)

        if len(positions) >= 6:
            depth = 5
        else:
            depth = 6

        for child_node in positions.keys():
            copy_of_table = get_children(child_node, positions.values(), computer, tabla)
            value = minimax_alpha_beta(copy_of_table, depth - 1, alpha, beta, False, vrijeme)
            max_eval = max(max_eval, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        positions = possible_positions(tabla, player)

        if len(positions) >= 6:
            depth = 5
        else:
            depth = 6

        for child_node in positions.keys():
            copy_of_table = get_children(child_node, positions.values(), player, tabla)
            value = minimax_alpha_beta(copy_of_table, depth - 1, alpha, beta, True, vrijeme)
            min_eval = min(min_eval, value)
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval


def is_terminal_node(copy_of_table):
    possitions = possible_positions(copy_of_table, computer)
    if game_over(copy_of_table):
        return True
    elif len(possitions) == 0:
        return True
    else:
        return False


def get_children(position, positions, color, copytable):
    copy_of_table = copy.deepcopy(copytable)

    tabla = possible_insert(color, position, positions, copy_of_table)

    return tabla


def over(color):
    if color == player:
        print("Computer won.")
    else:
        print("Player won.")

    exit()
