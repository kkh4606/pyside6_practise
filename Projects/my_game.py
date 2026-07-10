from colorama import Fore, Style


def display_board(d_board: list):

    print("+------+-----+------+")
    print(
        f"|  {Fore.GREEN+str(d_board[0])+Style.RESET_ALL}   |  {Fore.GREEN+str(d_board[1])+Style.RESET_ALL}  |   {Fore.GREEN+str(d_board[2])+Style.RESET_ALL}  |"
    )
    print("+------+-----+------+")
    print(
        f"|  {Fore.GREEN+str(d_board[3])+Style.RESET_ALL}   |  {Fore.GREEN+str(d_board[4])+Style.RESET_ALL}  |   {Fore.GREEN+str(d_board[5])+Style.RESET_ALL}  |"
    )
    print("+------+-----+------+")
    print(
        f"|  {Fore.GREEN+str(d_board[6])+Style.RESET_ALL}   |  {Fore.GREEN+str(d_board[7])+Style.RESET_ALL}  |   {Fore.GREEN+str(d_board[8])+Style.RESET_ALL}  |"
    )
    print("+------+-----+------+")


def check_winner(d_board: list):

    if d_board[0] == d_board[1] == d_board[2]:
        return d_board[0]
    elif d_board[0] == d_board[3] == d_board[6]:
        return d_board[0]
    elif d_board[1] == d_board[4] == d_board[7]:
        return d_board[1]

    elif d_board[2] == d_board[5] == d_board[6]:
        return d_board[2]
    elif d_board[0] == d_board[4] == d_board[8]:
        return d_board[0]

    return False


def check_tie(d_board: list):
    tie = False

    for i in d_board:
        if isinstance(i, str):
            tie = True
        else:
            tie = False

    return tie


def restart():
    rematch = input("Restart match (y/n)?: ").lower()
    if rematch == "y":

        return True
    return False


def match(d_board: list):

    p1_turn = True
    p2_turn = False

    times = 0

    while True:
        display_board(d_board)

        if p1_turn:

            try:

                p1_choice = int(input("Player One Turn: "))
            except ValueError:
                print("invalid input")
            else:

                print()

                if d_board[p1_choice - 1] not in ["X", "O"]:

                    d_board[p1_choice - 1] = "X"  # type: ignore
                    p2_turn, p1_turn = p1_turn, p2_turn

                    times += 1

        else:
            try:

                p2_choice = int(input("Player Two Turn: "))
            except ValueError:
                print("invalid input")
            else:

                print()
                if d_board[p2_choice - 1] not in ["X", "O"]:
                    d_board[p2_choice - 1] = "O"  # type: ignore
                    p1_turn, p2_turn = p2_turn, p1_turn
                    times += 1

        if times >= 5:
            winner = check_winner(d_board)

            if winner:
                display_board(d_board)
                print(winner, " Win!")

                if restart():

                    d_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    match(d_board)
                else:

                    break

        if times == 9:
            if check_tie(d_board):
                display_board(d_board)
                print("Tie")

                if restart():
                    d_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    match(d_board)
                else:

                    break


if __name__ == "__main__":
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    match(board)
