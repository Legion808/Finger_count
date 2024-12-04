#
#
# n = [1, 4, 6, "go", "sen"]
# m = ["uzb", 2, 5, 'men,', [23, 42332, "ad"]]
# c = "qanday jigar nima gap"
# k = ["men", "qachon", "kecha"]
# # print(m+n)
# # print(m[4][2])
# n = n.append("pkk")
# print(n)
# y = k.append("qanday")
# print(y)
#
# m = ['apple', 'car', 'cat']
# n = ["qanday", 'men', 'qachon']
# m.append(["sen", "qanday", "zormi"])
# print(m)
# m.insert(2, "good" )
# print(m)
# n.extend(m)
# print(n)

# n = int(input(" Enter the list obejects number "))
# m = []
# for i in range(n):
#     y = input()
#     m.append(y)
# print(" List objects ", m)

# m = "har doim insonlarga har yordam har ber"
# m = m.split("har", 3)
# print(m)

# n = input(" Enter the luky numers for list ").split()
# m = "45"
# m = int(m)
# print(n, m)

# n = input(" Enter the numbers for list please! ").split()
#
# for i in range(1, 3):
#     n[i] = int(n[i])
# print(n)

# n = ["faith", "good", "luck", 1, 3445, "Neil"]
# n[3] = 12345
# print(n)
# n[1:4] = ["men", "sen", "nega", "namoz"]
# print(n)
# n.insert(2, "harakat")
# print(n)

# n = ["faith", "good", "luck", 1, 3445, "Neil"]
# # n.remove("luck")
# # n.pop()
# # n.clear()
# del n
# print(n)


# #name search
# names1 = ["Diyor", "Behruz", "Muha", "Doston", "Bunyod", "Behzod"]
# b_names = []
# for name in names1:
#     if "B" in name:
#         b_names.append(name)
# print(b_names)
#
# d_names = [name1 for name1 in names1 if "D" in name1]
# print(d_names)
# name2 = names1.copy()
# print(name2)

# #5 ta istalgan sonli ro'yxat yarating va uni ekranga chiqaring
#
# a1 = [23, 23, 654, 234, 1]
# print(" Siz kiritgan ro'yxat ", a1)

# #append metodidan foydalanib, ro'yxatga yangi element qo'shing.
#
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# a1.append([" qanday zormi", 2])
# a1.insert( 2, ("salom", 'qanday'))
# a1.extend("asslom")
# print(" malumot ro'yxatga qo'shildi ", a1)

# # Ro'yxatdagi barcha elementlarni bir qatorda ekranga chiqaring.
#
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# a2 = "Men har doim senga ishonman "
# print(" ".join(map(str, a1)))

# # Ro'yxatdagi elementlar sonini len yordamida toping.
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# a2 = "salom har"
# print(len(a1))
# print(len(a2))

# # Ro'yxatning ikkinchi elementini ekranga chiqaring.
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# print(a1[::-1])

# #Ro'yxatni reverse yordamida teskari qiling.
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# a1.reverse()
# print(a1[::-1])
# print(a1)

# # remove yordamida ro'yxatdan ma'lum bir elementni o'chiring.
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# # a1.remove("back")
# # a1.clear()
# # del a1
# a1.pop(1)
# print(a1)

# #Element ro'yxatda mavjudligini in operatori yordamida tekshiring.
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
#
# if "Cu" in a1:
#     print(" List object ")
# else:
#     print(" Not list object")

# #Ikkita ro'yxatni + operatori bilan birlashtiring.
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# a2 = ["pray", 'go', 34, 'goal', 2]
# a1.extend(a2)
# # print("List elements added ", a1+a2)
# print(a1)

# #Ro'yxatdagi eng kichik va eng katta qiymatni toping.
# a1 = [23, 454, 12, 345, -1, "fshf", "243ruhjfis"]
# min_a1 = a1[0]
# max_a1 = a1[0]
#
# int_v = [n for n in a1 if isinstance(n, int)]
# print(min(int_v), max(int_v))
# # for s in a1:
# #     if s>max_a1:
# #         max_a1 = s
# #     if s<min_a1:
# #         min_a1 = s
# #
# # print(max_a1, min_a1)

# #Ro'yxatni saralash: sort metodidan foydalanib, ro'yxatni o'sish tartibida saralang.
# a1 = [23, 454, 12, 345, -1, 12, 345]
# a1.sort(key=int, reverse=True)
# print(a1)

# #Yangi ro'yxat yaratish: Ro'yxatdagi juft sonlardan yangi ro'yxat yarating.
#
# a1 = [23, 454, 12, 345, -1, 12, 345]
# a2 = [n for n in a1 if n%2==0]
# print(a2)

# #Index aniqlash: index metodidan foydalanib, ma'lum bir elementning indeksini toping.
#
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# print(a1.index("car", 1, 4))
# print(a1)

# #Har bir elementni 2 ga ko'paytirib, yangi ro'yxat yarating.
# a1 = [23, 454, 12, 345, -1, 12, 345]
#
# a2 = [n*2 for n in a1]
# print(a2)

# #Ro'yxatni kesish: Ro'yxatning biror qismini kesib olish (masalan, birinchi 3 elementni ajratib olish).
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# print(a1[:3])

# #Ro'yxatdan takrorlanuvchi elementlarni olib tashlab, faqat unikal elementlardan iborat yangi ro'yxat yarating.
#
# a1 = [23, 454, 12, 345, -1, 12, 345, 12]
# a2 = []
# for n in a1:
#     if n not in a2:
#         a2.append(n)
# print(a2)
#
# a3 = list(set(a1))
# print(a3)

# #Ro'yxatning oxirgi elementini birinchi o'ringa ko'chiring.
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# # a2 = a1[-1]
# # a1.pop(-1)
# # a1.insert(0,a2)
# # print(a1)
# a3 = [a1[-1]]+a1[:-1]
# print(a3)

# # 3x3 o'lchamdagi sonli ro'yxat yarating va uni ekranga chiqaring.
#
# a1 = ['num', 23, ['dad', ['dajd', 23], 'dsf']]
# print(a1[2][1][1])
# a2 = [
#     [11, 22, 33],
#     [33, 44, 55],
#     [66, 77, 88]
# ]
#
# for n in a2:
#    print(n)
#
# i = sum(sum(row) for row in a2)
# d = [a2[i][i] for i in range(3)]
# print(i, d)
# print(a2[1])
# s = [row[1] for row in a2]
# print(s)

#Ro'yxatni teng ikki qismga ajrating.

# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
#
# e_i = len(a1)//2
# e1 = a1[:e_i]
# e2 = a1[e_i:]
#
# print(" teng bo'lingan ro'yxatlar \n", e1, "\n", e2)

# #Elementlar yig'indisi: Ro'yxatdagi barcha sonlarning yig'indisini hisoblang.
# a22 = [32, 43, 2, 5, 23]
# a1 = ["Cut", 'car', 'look', 'back', 12, 345]
# a2 = sum(m for m in a22)
# a3 = sum(n for n in a1 if isinstance(n, int))
# print(a3)
# print(a2)

# #: Bitta ro'yxatda ichma-ich bir nechta kichik ro'yxatlar yarating va ularni ekranga chiqaring.
#
# a1 = ["good", 12, "2442", [32, "dag", "gda", ["why", 13, "back"]]]
#
# print(a1[3][3][2])
#
# a2 = [
#     ["Math", [11, 22, 33]],
#     ["Phy",  [53, 25, 35]],
#     ["Alg",  [13, 75, 67]],
# ]
# for sub in a2:
#     print(f"{sub[0]} - Fanidan : {sub[1]} - ball")

#

# a2 = [
#     [11, 22, 33],
#     [53, 25, 35],
#     [13, 75, 67],
# ]
# a1 = [n[::-1] for n in a2[::]]
#
# for n in a1:
#     print(n)

# # matritsani 90 gradusga burush
# n = [list(m) for m in zip(*a2[::-1])]
# for m in n:
#     print(m)
#
# print(a2[::-1])

# #Ikkita ro'yxatda mavjud bo'lgan o'xshash elementlarni toping.
#
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# a2 = [23, 454, 12, 345, -1, 12, 345, 'back', 12]
#
#
# # l = []
# # for a in a1:
# #     for b in a2:
# #         if a==b not in l:
# #             l.append(a)
# # l = list(set(a1) & set(a2))
# l = [m for m in a1 if m in a2]
# print(l)

# # Ranglardan iborat ro'yxat yaratib, uni alfavit bo'yicha saralang.
#
# a1 = ["oq", "qizil", "sariq", "kok", "qora"]
# a1.sort(key=str, reverse=True)
# print(a1)

# #Ro'yxat elementlarini almashtirish: Ro'yxatdagi ikkita elementning o'rnini almashtiring.
#
# a1 = ["Cut", 'car', 'look', 'back', 12, '345']
# a2 = [23, 454, 12, 345, -1, 12, 345, 'back', 12]
# a1[2], a2[-1] = a2[-1], a1[2]
# print(a1, a2)

# #Ro'yxatni kamayish tartibida saralang va natijani chiqaring.
#
# a2 = [23, 454, 12, 345, -1, 12, 345, 12]
# a2.sort(key=int, reverse=True)
# print(a2)

#Ichma-ich ro'yxatdagi eng katta qiymatni toping.
#
# a1 = [-2, 12, 321.4, [32, 5, 90, [-23, 13, 0.3]]]
# l1 = [[3, 5, 7], [1, 6, 9], [4, 8, 2]]
# l = max([n for m in l1 for n in m])
# b = max(map(max, l1))

# def find_max(lst):
#     m = float('inf')
#
#     for n in lst:
#         if isinstance(n, list):
#             m = min(m, find_max(n))
#         else:
#             m = min(m, n)
#     return m
# m = find_max(a1)
# print("max value ", m)
#
# # print(l, b)
#
# # fibonachi sonlar
# def fibo(n):
#     a2 = [23, 454]
#     for i in range(2, n):
#         l = a2[i - 1] + a2[i - 2]
#         a2.append(l)
#     return a2
#
# n = 10
# print(fibo(n))


# a2 = [
#     [11, 22, 33],
#     [53, 25, 35],
#     [13, 75, 67],
# ]
# l = [sum(n) for n in a2]
# print(l)

