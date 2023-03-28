import random as rand
import time

rand.seed(time.time())

instructions = "Use keys to choose next move:\n" \
               "q w e\n" \
               "a s d\n" \
               "z x c\n" \
               "Key: "

move_map = {'q': 0, 'w': 1, 'e': 2,
            'a': 3, 's': 4, 'd': 5,
            'z': 6, 'x': 7, 'c': 8}

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

win_cond = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]]  # diagonal


def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}\n"
          "----------\n"
          f"{board[3]} | {board[4]} | {board[5]}\n"
          "----------\n"
          f"{board[6]} | {board[7]} | {board[8]}\n")


# insert 'X' or 'Y' at win loc in win_cond list
def insert_wincond(val, loc):
    for w in win_cond:
        for i in range(3):
            if w[i] == loc:
                w[i] = val


# bot doesn't play to win, plays to block (mostly)
def bot_move():
    # rank each available move
    move_rank = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        rank = 0
        for w in win_cond:
            if i in w:
                # player goofed, rank to guarantee winning move
                if w.count('Y') == 2:
                    rank = 100
                # rank move based on how many 'X's are in winning condition
                elif w.count('X') == 2:
                    rank += 2
                rank += 1
        move_rank[i] = rank

    # find max ranked moved value
    max_rank = max(move_rank)
    move_list = [i for i in range(len(move_rank)) if move_rank[i] == max_rank]  # create list of max moves
    mv = rand.choice(move_list)  # choose random from max rank moves
    board[mv] = "Y"
    insert_wincond("Y", mv)


def game_finished():
    # check win conditions
    for i in ['X', 'Y']:
        for w in win_cond:
            if w.count(i) == 3:
                print(f'Game over - {i} wins')
                print_board()
                return True

    if board.count(" ") == 0:
        print_board()
        print("Game over - Tie")
        return True
    return False


# game loop
done = False
while not done:
    print_board()
    move = input(instructions)
    if move in move_map and board[move_map[move]] == " ":
        board[move_map[move]] = "X"
        insert_wincond("X", move_map[move])
        bot_move()
        done = game_finished()
    else:
        print("invalid move")
