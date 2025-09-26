# # try_and_except
# try:
# number = int(input("Son kiriting: "))
# print("Bu son", number ** 2)
# except:
#     print("noto'g'ri element")

# try:
#     print(x)
# except:
#     print("Bunday o'zgaruvchi mavjud emas")

# print(x)

# try:
#     son = int(input("Son kiriting: "))
#     print(10 / son)
# except ZeroDivisionError:
#     print("0 ga bolinmaydi")
# # oxirgi qiymat uchun
# except:
#     print("Noto'g'ri element")
# else:
#     print("To'g'ri son kiritingiz")

# finally:
#     print("Dastur ishlashdan to'xtadi")

# def sum_of_list(numbers):
#     return sum(numbers)

# try:
#     sum_of_list(numbers) == 171
#     print(f"Natija {sum_of_list(numbers)}")
# except:
#     print("Hisoblab bo'lmaydi")

try:
    numbers = [34,56,45,36]
    print(numbers[6])
except IndexError:
    print("Noto'g'ri index")

# numbers = [34,56,45,36]
# print(numbers[6])