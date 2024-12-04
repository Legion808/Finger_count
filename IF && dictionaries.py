# a  = {"Brand": "Iphone", "Ram": "256", "Memory": "256"  }
#
# print(a.keys())
# print(a.values())
# print(a.items())
# print(a.get("Ram"))
#
# a["Model"] = "Q234"
# a["Ram"] = "Q3444"
# print(a)
#
# # a.pop("Brand")
# # a.popitem()
# # del a["Ram"]
# # a.clear()
#
# b = a.copy()
# c = a.__dict__
# print(b)
# import random

#Tuple

# a = ("leg", 12)
#
# print(a[1:])
#
# a = {"Ism ": "Diyor", " Yosh": "22", "Field": "Web" }
# b = {"Bilim": "Smart", "Level": " senior"}
# # print(a["Ism "])
# # print(a.keys())
# # print(a.values())
# # print(a.items())
# # print(a.get("Ism "))
# # a["Manzil"] = "Toshkent"
# # print(a)
# # a.pop(" Yosh")
# # print(a)
# # print(a.get("Email"))
# # a["Ism "] = "Mike"
# # print(a)
# # l1 = a.copy()
# # l1.update(b)
# # print(l1)
# # l2 = {**a, **b}
# # print(l2)
# # c = dict(sorted(a.items(), key=lambda item: item[1], reverse=True))
# a["Ism "] = {"Men": "Malish"}
# print(a)
# print(a["Ism "])
#
# #Tuple
# a = ("har", 3, 32, ("har", ("2435", "fgdfh")), 42)
# b1 = ("har", 3, 32, ("har", ("2435", "fgdfh")), 42)
# print(a[1],a[3])
# # del a
# # b = ()
# # a = a.count("har")
# # c = len(a)
# # b = len(list(a))
# b = tuple(list(a)+list(b1))
# print(b)
# a = list(a)
# b = tuple(a[:(len(a)//2)])
# s = tuple(a[(len(a)//2):])
# print("Birinchi tuple 1 ", b)
# print("ikkinchi tuple 2 ", s)
#
# print(b1[3][1][0])

#if operator

# x = float(input(" Enter the number "))
# print("Musbat son") if x>=0 else print("Manfiy son")

# #Ikkita sonni solishtirib, kattasini chiqar.
# x = float(input(" Enter the number 1: "))
# y = float(input(" Enter the number 2: "))
#
# print("Katta son ", x) if x>y else print(" Katta son ", y)
# if x>y:
#     print("Katta son ", x)
# elif x==y:
#     print(" teng sonlar ", x, y)
# else:
#     print(" Katta son ", y)

# #Son 3 ga yoki 5 ga bo'linishini tekshiring.
#
# x = float(input(" Enter the number 1: "))
# print(" 3 yoki 5 ga bo'linadi" ) if x%3==0 or x%5==0 else print(" Bu sonlar 3 va 5 ga bo'linmaydi")
#

# #Son 10 va 50 orasida ekanligini tekshiring.
# x = float(input(" Enter the number 1: "))
# print("10 va 50 orasida ") if 10<x<50  else print("10 va 50 orasida  emas ")

# #Lug'atda telefon kaliti mavjudligini tekshiring
#
# l = ["salom", "kecha", "bugun", "telefon", "13"]
# x = input(" Enter the value: ")
# s = [print(f"{x} list ichida mavjud") for n in l if x in n]
# if not s:
#     print("mavjud emas")

# a = input(" Matnni kiriting unli va undosh harflarni hisoblaymiz \n")
# unli_harflar = "aeiouAEIOU"
# undosh_harflar = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# u1 = 0
# u2 = 0
# for n in a:
#     if n in unli_harflar:
#         u1+=1
#     elif n in undosh_harflar:
#         u2+=1
# print("Unli harflar soni ", u1)
# print("Undosh harflar soni " , u2)
# print(set(a))

# #Foydalanuvchi oyning raqamini kiritsin (1-12), unga mos faslni chiqaring.
# n = float(input(" Oy raqamini kiriting "))
# if 1<=n<=2:
#     print(" Hozirgi fasl qish")
# elif 3<=n<=5:
#     print(" Hozirgi fasl Bahor")
# elif 6<=n<=8:
#     print(" Hozirgi fasl Yoz")
# elif 9<=n<=11:
#     print(" Hozirgi fasl Kuz")
# else:
#     print("Hozirgi fasl Qish")

# # Foydalanuvchidan uch xonali son kiriting va uning raqamlari yig'indisini tekshirib, juft yoki toqligini aniqlang.
# n = input(" Enter the triple number  ")
# # m = n//100
# # m1 = (n//10)%10
# # m2 = n%10
# # s = m+m1+m2
#
# l = sum(int(b) for b in n)
# if l%2==0:
#     print(" Siz kiritgan raqamlar yigindisi juft ", l)
# else:
#     print(" Siz kiritgan raqamlar yigindisi toq ", l)

# #Foydalanuvchi valyuta nomini (USD, EUR, GBP) kiritsin va miqdorni so'mga konvertatsiya qiling.
# n = input(" Enter the valyuta ")
# if n == "USD":
#     m = int(input(" Qiymatni kiriting "))
#     print("Sumdagi bahosi = ", m*12750)
# elif n == "EUR":
#     m = int(input(" Qiymatni kiriting "))
#     print("Sumdagi bahosi = ", m * 13850)
# elif n == "GBP":
#     m = int(input(" Qiymatni kiriting "))
#     print("Sumdagi bahosi = ", m * 15803)
# else:
#     print(" Bunday valyuta mavjud emas")

# # Foydalanuvchi 1 dan 10 gacha son kiritsin. Tasodifiy son bilan solishtirib, yutgan yoki yutmaganini aniqlang.
# m = random.randint(1,10)
# n = int(input(" Omadli sonni kiriting "))
# print(m)
# print("Lotereyada golib boldingiz ", n) if n==m else print("Omadni qayta sinab ko'ring ")
#


# #Foydalanuvchidan kasr son kiriting. Uning butun va kasr qismini aniqlang, keyin butun qismi juft yoki toq ekanligini tekshiring.
#
# n = float(input(" Kasr sonni kiriting "))
# k = n%1
# b = n//1
# print(" Sonning butun qismi ", b)
# print(" Sonning kasr qismi ", k)
# print(" Butun qismi juft ", b) if b%2==0 else print(" Butun qismi toq", b)
#

# #To'rt xonali son kiriting va uning birinchi va oxirgi raqamlari yig'indisini tekshiring.
#
# n = input(" Kasr sonni kiriting ")
# m = int(n[0])+int(n[-1])
# print(m)


l = [1, 2, 5]
b = [3, 5, 8]
print(l+b)


print(len([sum([1,1,1])]))

a = 1
b = 0
print(a/b)
