# # range - bu bizda raqamlarni shaklantirish uchun ishlatiladi
# # 2 ta argument qabul qiladi 
# # 1. start - boshlanishi
# # 2. end - tugashi

# # numbers = [1,2,3,4,5]
# # numbers2 = range(1, 5)
# # print(f"Bu list bilan {numbers}")
# # print(f"Bu range bilan chiqan natija {numbers2}")

# # index = int(input("Index kiriting: "))
# # fruits = ['apple', 'banana', 'cherry', "Anor", "Tarvuz"]
# # for number in range(0, len(fruits)):
# #     if index == number:
# #         print("Bu maxsulat ro'yxatda bor")
    
# #     elif index > number:
# #         print("Bu ro'yxatda mavjud emas")


# # for x in range(0, 10 + 1):
# #     print(x)

rows = [rows for i in range(8)]


# def get_only_evens(numbers):
#     new_index_number = []
#     for index, number in enumerate(numbers):
#         if index % 2 == 0 and number % 2 == 0:
#             new_index_number.append(number)

#     return new_index_number

# print(get_only_evens([1, 3, 2, 6, 4, 8]))
# print(get_only_evens([0, 1, 2, 3, 4]))

# # 4-vazifa. (Even All the Way).
# def get_only_evens(numbers):
#     return [number for index, number in enumerate(numbers) if index % 2 == 0 and number % 2 == 0]

# print(get_only_evens([1, 3, 2, 6, 4, 8]))
# print(get_only_evens([0, 1, 2, 3, 4]))
# print(get_only_evens([1, 2, 3, 4, 5]))

# board = [["EMPTY" for x in range(8)] for x in range(8)]
# for x in range(8):
#     row = ["EMPTY" for x in range(8)]
#     board.append(row)

# board[0][0] = "ROOK"
# board[0][7] = "ROOK"
# board[7][0] = "ROOK"
# board[7][7] = "ROOK"

# board[4][2] = "KNIGHT"
# board[3][4] = "PAWN"

# temps = [[0.0 for hours in range(24)] for days in range(31)]

# print(temps)