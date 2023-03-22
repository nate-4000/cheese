import stockfish


whereFish = input("wheres my fish? ")
x = stockfish.Stockfish(whereFish)

curplayer = True # white

repre = {
    True: "White",
    False: "Black"
}

while True:
    x.make_moves_from_current_position([x.get_top_moves()[0]["Move"]])
    curplayer = not curplayer
    print("%s's move" % (repre[curplayer]))
    print(x.get_board_visual())
    if x.get_top_moves()[0]["Mate"]:
        break

print("Mate")

