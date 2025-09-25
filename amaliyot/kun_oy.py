# def find_days(year, month):
#     days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
#     if month < 1 and month > 12:
#         return None 

#     return days[month - 1]
    
# print(find_days(2024, 3))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 20 gacha tub sonlarni chiqaramiz
for i in range(2, 20):
    if is_prime(i):
        print(i, end=" ")

print(is_prime(20))