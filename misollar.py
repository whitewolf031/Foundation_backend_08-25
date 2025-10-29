# # def sezor_shifrlash(text):
# #     alphabet = list("abcdefghijklmnopqrstuvwxyz")
# #     for word in text:
# #         if word in alphabet:
# #             index = alphabet.index(word)
# #             natija += alphabet[(index + 1)]

# # text = input("Sozni kiriting: ")
# # print(sezor_shifrlash(text))


# # sana = input("tug'ulgan kuningni kirit: ")
# # raqamlar_yigindisi = 0
# # for raqam in sana:
# #     if raqam.isdigit():
# #         raqamlar_yigindisi += int(raqam)
# # while raqamlar_yigindisi > 9:
# #     yigindi = 0
# #     for raqam in str(raqamlar_yigindisi):
# #         yigindi += int(raqam)
# #     raqamlar_yigindisi = yigindi
# # print(raqamlar_yigindisi)

# # def led():
# #     a1 = [
# #         "  #",
# #         "  #",
# #         "  #",
# #         "  #",
# #         "  #"
# #     ]
# #     a2 = [
# #         "###",
# #         "  #",
# #         "###",
# #         "#  ",
# #         "###"
# #     ]
# #     a3 = [
# #         "###",
# #         "  #",
# #         "###",
# #         "  #",
# #         "###"
# #     ]
# #     a4 = [
# #         "# #",
# #         "# #",
# #         "###",
# #         "  #",
# #         "  #"
# #     ]
# #     a5 = [
# #         "###",
# #         "#  ",
# #         "###",
# #         "  #",
# #         "###"
# #     ]
# #     a6 = [
# #         "###",
# #         "#  ",
# #         "###",
# #         "# #",
# #         "###"
# #     ]
# #     a7 = [
# #         "###",
# #         "  #",
# #         "  #",
# #         "  #",
# #         "  #"
# #     ]
# #     a8 = [
# #         "###",
# #         "# #",
# #         "###",
# #         "# #",
# #         "###"
# #     ]
# #     a9 = [
# #         "###",
# #         "# #",
# #         "###",
# #         "  #",
# #         "###"
# #     ]
# #     a0 = [
# #         "###",
# #         "# #",
# #         "# #",
# #         "# #",
# #         "###"
# #     ]

# #     kod = {1:a1, 2:a2, 3:a3, 4:a4, 5:a5, 6:a6, 7:a7, 8:a8, 9:a9, 0:a0}

# #     number = input("Raqamni kiriting: ")
# #     satrlar = ["", "", "", "", ""]

# #     for n in number:
# #         n = int(n)
# #         if n in kod:
# #             led1 = kod[n]
# #             for i in range(5):
# #                 satrlar[i] += led1[i] + "  "

# #     return "\n".join(satrlar)


# # print(led())

# def m():
#     a= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     b= ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010']
    
#     matn = input("matini kiriting = ").upper()
#     shifr = dict(zip(a,b))
#     matinlar = dict(zip(b,a))

#     if all(x.isalpha() or x.isspace() for x in matn):
#         natija=[]
#         for harf in matn:
#             if harf in shifr:    
#                 natija.append(shifr[harf])
#             elif harf == " ":
#                 natija.append("/")
#         return " ".join(natija)
        
#     else:
#         soz = matn.split()
#         natija = []
#         for kod in soz:
#             if kod in matinlar:
#                 natija.append(matinlar[kod])
#             elif kod == "/":
#                 natija.append(" ")
#         return "".join(natija).capitalize()
    
# print(m())