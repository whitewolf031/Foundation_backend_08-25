# dict
# bu mutable (o'zgaruvchan) ma'lumot turi
# print(dictionary["cat"])

# phone_numbers = {54678: 789465, "Suzy": 7854218965, "Bobur": 789465132, "Suzy": 897654132}
# print(phone_numbers)
# print(dictionary.items())
# print(dictionary["president"])

# # empty_dict = {}
# # print(type(empty_dict))

# for key, value in dictionary.items():
#     print(key, "->", value)

# print("Mushuk" in dictionary)
# dictionary = {"cat": "Mushuk", "dog": "it", "horse": "ot"}
# words = ["cat", "lion", "horse"]
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")

dictionary = {
    "cat": "Mushuk", 
    "dog": "it", 
    "horse": "ot"
}

# print(dictionary.keys())
# print(dictionary.values())
dictionary["cat"] = "Pishak"
dictionary["duck"] = "O'rdak"
print(dictionary)

