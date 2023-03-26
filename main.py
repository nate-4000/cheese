import stockfish
import time
import random

def intput(name):
    """
    thanks to stackoverflow
    """
    global value
    value = input(name)
    while not value.isnumeric():
        print("enter a number")
        value = input("enter again")
    return int(value)


def detectffrep(lst):
    """
    thank you ChatGPT for writing this, big much very thanks
    """
    count = 1
    for i in range(len(lst) - 1):
        if lst[i] == lst[i+1]:
            count += 1
            if count > 5:
                return True
        else:
            count = 1
    return False


whereFish = input("wheres my fish? ")
x = stockfish.Stockfish(whereFish)

curplayer = True # white

repre = {
    True: "White",
    False: "Black"
}

game = []

while True:
    best = x.get_top_moves()
    bestweights = []
    for i in best:
        bestweights += [i["Centipawn"]]
    # print(best[0], flush=False)
    x.make_moves_from_current_position([best[0]["Move"]])
    curplayer = not curplayer
    print("%s's move" % (repre[curplayer]), flush=False)
    print(x.get_board_visual())
    game += [x.get_fen_position()]
    if best[0]["Mate"] or detectffrep(game):
        break

if not detectffrep(game):
    print("Mate")
else:
    print("Repeated game")
with open("game_%d.fen" % ( int(time.time())), "a") as file:
    for i in game:
        file.write(i + "\n")