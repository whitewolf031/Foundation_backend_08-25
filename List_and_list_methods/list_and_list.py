# row = ("WHITE_PAWN" for i in range(8))

# for number in range(8):
#     row.append("WHITE_PAWN")

# # print(list(row))

# # squares = [x ** 2 for x in range(10)]
# # print(squares)

# for x in range(10):
#     print(x ** 2)

# squares = [1, 2, 4, 8, 16, 32, 64, 128]
# odds = [x for x in squares if x % 2 == 0]
# for x in squares:
#     if x % 2 == 0:
#         print(x)

# board = [['EMPTY'] for i in range(8 + 1) for j in range(8 + 1)]
# board[0][0] = "ROOK"
# board[7][0] = "ROOK"

# print(board)
# boards = []
# for i in range(8):
#     row = ['EMPTY' for i in range(8)]
#     boards.append(row)

# boards[0][0] = "ROOK"
# boards[0][7] = "ROOK"

# print(boards)

# rooms = [[[False for room in range(20)] for floor in range(15)] for hotel in range(3)]
# rooms[1][9][19] = True
# print(rooms[1][9][19])

# rooms = []
# for hotel in range(3):
#     rooms.append(False)
#     for floor in range(15):
#         rooms.append([False])
#         for room in range(20):
#             rooms.append([[False]])
# print(rooms)