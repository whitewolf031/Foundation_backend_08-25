# # list = bu ro'yxat
# # [] - bu boldimi list
# # print(mevalar)
# # print(type(mevalar))
# # print(mevalar[1])
# # print(mevalar[:])
# # print(mevalar[::-1])
# # print(mevalar[-1])

# # del mevalar[-1]
# # print(mevalar)
# m = True
# n = str(m)
# print(list(n))

# # mevalar = ["Olma", "Anor", 'tarvuz', "Qovun", "Banan", m]
# # mevalar.append("Nok")
# # mevalar.insert(1, "Uzum")
# # print(mevalar)

# bazi bir malumot turlarini listga tog'ridan to'g'ri o'tkizib bomidi (int, bool)
# methodlar - bu list ichidagi ma'lumotlarni 
# o'zgartirish uchun ishlatiladi

# sabzavotlar = ["Sabzi", "Bodring", "Pamidor"]
# royxat = []
# for meva in mevalar:
#     royxat.append(meva)
#     for sabzavot in sabzavotlar:
#         royxat.append(sabzavot)

# print(royxat

# tozalash
# mevalar.clear()
# print(mevalar)

# nusxalash
# m = mevalar.copy()
# print(m)

# ma'lumotlarni sanash
# m = mevalar.count("Olma")
# print(mevalar)

# index ni korish
# n = mevalar.index("Banan")
# print(f"Bu uning index {n}")

# index orqali kesib olish
# qaychi = mevalar.pop(2)
# print(qaychi)
# print(mevalar)

# o'chirish
# mevalar.remove("Qovun")
# print(mevalar)

# teskari qilish
# mevalar.reverse()
# print(mevalar)
# print(mevalar[::-1])

# ketma ket tartiblash
# mevalar.sort()
# print(mevalar)

# mevalar = ["Olma", "Anor", 'tarvuz', "Qovun", "Banan"]
# royxat = ["Banan"]
# for meva in mevalar:
#     if meva not in royxat:
#         royxat.append(meva)

#     elif meva in royxat:
#         print("Bu royxatda bor")

# print(royxat)

numbers = [1,2,3,4,5]
# eng kattasi
print(max(numbers))
# eng kichigi
print(min(numbers))
# har bir elementni qoshib chiqaradi
print(sum(numbers) / 5)
