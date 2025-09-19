# return dan foydalanishni 2 xil usuli 
# 1. qiymat qaytarmaslik 
# 2. oxirgi qiymat

# 1. holat
# def happy_new_year(wishes):
#     print("Three....")
#     print("Two....")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy New Year")

# happy_new_year(True)

# 2 - xolat 
# def boring_function():
#     print("'Boredom mode' On.")
#     return 123

# print("This lesson is interesting!")
# boring_function()
# print("This lesson is boring....")

# print(values + 2)
# lst = []
# soz = " "
# print(type(value))
# print(type(soz))

# value = None
# if value is None:
#     print("Bu yerda malumot yo'q")
# print(f"Bu yerda hozir bosh qator {None}")

# def strange_function(number):
#     if number % 2 == 0:
#         return True

# print(strange_function(2))
# print(strange_function(1))

def list_sum(numbers):
    # s = 0
    new_list = []
    for element in numbers:
        if element % 2 == 0:
            new_list.append(element)
    #     s = s + element
    return new_list

print(list_sum([5,4,3,6,5,3]))
print(list_sum(5))



