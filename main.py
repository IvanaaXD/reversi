from reversi import print_table, count, game_over, player1_move, computer_move, check_who_won, table

if __name__ == '__main__':

    print_table(table)
    count()

    while not game_over(table):
        player1_move()
        count()
        # player2_move()
        computer_move()
        count()

    check_who_won()
