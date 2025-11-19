# # Nomli funksiya
# def hisobla(x, y):
#     return x + y

# print(f"Bu nomli funksiya {hisobla(4,2)}")

# # Nomsiz funksiya
# qoshish = lambda x, y: x + y

# print(f"Bu nomsiz funksiya {qoshish("Hello ", "World!")}")

# def fun(n):
#     # generatorlar bu range
#     # iteratorlar bu for sikl in
#     for x in range(n):
#         yield x

# for x in fun(5):
#     print(x)

# Functional programming
# lampbda
# map - 
# filter
# reduce


# map
# 2 argument qabul qiladi
# 1. funksiya
# 2. ma'lumot turi
# raqamlar = [1,2,3,4,5,6,7,8,9,10]
# print(raqamlar)
# # listni ichidagi ma'lumotlar ni o'zgartirish
# new_natija = list(map(lambda x: x ** 2, raqamlar))
# print(new_natija)


# filter
# 2 argument qabul qiladi
# 1. funksiya
# 2. ma'lumot turi
# raqamlar = [0,1,2,3,4,5,6,7,8,9,10]
# filtrlangan_malumot = list(filter(lambda x: x % 2 != 0, raqamlar))
# print(filtrlangan_malumot)

# reduce
# 2 argument qabul qiladi
# 1. funksiya
# 2. ma'lumot turi

# from functools import reduce
# grades = [3,4,5,2]
# new_grades = reduce(lambda x, y: x ** 0.5, grades)
# print(new_grades)