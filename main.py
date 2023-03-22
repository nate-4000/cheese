import stockfish


whereFish = input("wheres my fish? ")
x = stockfish.Stockfish(whereFish)

while not x.get_top_moves()[0]["Mate"]:
    x.make_moves_from_current_position([x.get_top_moves()[0]["Move"]])
    print(x.get_board_visual())