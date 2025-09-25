# # sequences - ketma-ketlik

# # o'zgaruvchan - mutability
# # o'zgarmas - immutable

# # lst = [1,2,3,4,5,6,7,8,9,10]
# # lst[6] = 15
# # print(lst)

# # x = 1
# # m = tuple(lst)
# # n = list(m)
# # print(m)
# # print(n)
# # tuple_1 = (1,2,3,4,5,6,7,8,9,10)
# # # tuple_1.append(15)
# # # del tuple_1[3]
# # # tuple_1[6] = 15
# # print(tuple_1[6])
# # print(tuple_1)

# tuple_2 = ("hello", 3.5, 2, 4, "Sardor uyga vazifa yoq Bobur bilan birga", "Hello")
# tuple_3 = 1,2,3,4,5,6,7,8,9,10
# #         0,1,2,3,4,5,6,7,8,9
# # tuple_3.copy()
# # # print(tuple_2)

# # empty_tuple = ()
# # print(tuple_2)
# # print(type(tuple_2))

# # print(len(tuple_2))
# # print(tuple_2 + tuple_3)
# # print(sum(tuple_3))
# # print(tuple_3.index(1))
# # print(tuple_2.count("hello"))
# # print(tuple_2 * 3)
# # print(4 in tuple_3)
# # print(4 not in tuple_3)
# print(tuple_3[6])

# var = 2
# t1 = (1,)
# t2 = (2,)
# t3 = (3, var)
# t1, t2, t3 = t2, t3, t1
# print(t1, t2, t3)

