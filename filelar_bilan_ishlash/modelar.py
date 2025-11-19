# file ochish uchun 2 ta narsa kerak
# 1. open()
# 2. mode:
    #1. x
    #2. w
    #3. a
    #4. r
    #5. r+
    #6. w+
# 3. close()

# x - faqat fayl ochish
# file = open("my_first_file1.txt", mode="x")
# print(f"fayl yaratildi {file}")

# w - write vazifasi file ochish va yozish
# file = open("my_second_file.doc", "w")
# file.write("Salom ")
# file.write("Bobur")
# file.close()

# a - append - qoshish 
file = open("Amirxon.txt", "a")
file.write("print('Hello world!')\n ")
file.close()


# file = open("/home/sardorbek/Desktop/file.txt", "a+")
# file.write("Bobur gaplashmay o'tir")
# print(file.read())

# with open("Amirxon.txt", "r") as f:
#     # f.write("Hello world! ")
#     f.seek(35)
#     text = f.read()
#     print(text)

import os

# # os.remove("my_file.txt")
# os.removexattr("/home/sardorbek/Documents/Foundation_backend_08-25/my_second_file.doc", "sardorbek.comment")

# print(os.name)

# import os
# os.mkdir("my_first_directory/my_second_directory")
# os.removedirs("my_first_directory/my_second_directory")
# print(os.listdir())

# import os
# returned_value = os.system("mkdir my_first_directory")
# print(returned_value)

import calendar

c = calendar.Calendar()

for d in c.itermonthdates(2019, 11):
    print(d)
