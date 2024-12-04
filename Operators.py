# # Sonlar ustida arifmatik amallar
#
# a = 10
# b = 5
# print(" Qo'shildi ", a+b, f" \n Ayirish ",  a-b, f"\n Ko'paytirildi ", a*b, f"\n Devission ",a/b, f" \n Qoldiqli bolish ", a%b, a//b, a**b)


# #Ikkita sonni o'zaro tengligiga tekshirish
#
# x = 110
# y = 110
# if x==y:
#     print(" Bu sonlar o'zaro teng ")
# else:
#     print(" Bu sonlar teng emas ")
#

# #Assigment topshiriq
# num = 10
# num += 5
# num *= 2
# print(" Natija ", num)

# # Bitwise amallar
# n = 8
# m = 5
# print(bin(n), bin(m))
# x = n&m
# y = n|m
# z = n^m
# print(" All bitwise amallar ", bin(x), bin(y), bin(z) )

# #listdan malumotlarni tekshirish
#
# list1 = [23, 14, 432, 533, 5, 62, 68]
# m = 23
# a = 32456
# s = m in list1
# n = a not in  list1
# print(s, n)

#
# # ikkita o'zgaruvchini bitta obyekt ekanligini tekshirish is id orqali tekshirish
# a = 5
# b = 5
# c = 10
# a1 = [1, 2, 3]  #har doim list saqlangan hotira id si bir xil bo'lmaydi
# a2 = [1, 2, 3]
# m = a is b is not c
# n = a1 is  not a2
# print(m, n)

# #ikkilik binar qilish
# n = 12
# print(bin(n))

# # exlicit ikki sonni almashtirish va typelarni tanlash
#
# a = "12"
# b = 34.5
# # a1 = int(a)
# a, b = b, a
# print(f" Butun son ko'rinishida ", int(a), int(b))
# print(f" Haqiqiy son ko'rinishida ", float(a), float(b))

# #Comparison , berilgan son musbat yoki manfiy ekanligi yoki 0
# n = -142
# if n>0:
#     print(" Musbat son")
# elif n==0:
#     print(" o ga teng son")
# else:
#     print(" manfiy son")

# #To'rtburchak yuzi va parametri
# a = 5
# b = 10
# s = a*b
# p = 2*(a+b)
# print(" Yuzi ", s, f" \n Parametri ", p)

# #and va or bilan manfiy yoki musbatga tekshirish
# a = 7
# b = 2
# c = -3
# if a>0 and b>0 and c>0:
#     print(" Barcha sonlar musbat ")
# else:
#     print(" Manfiy son mavjud")
#
# if a>0 or b>0 or c>0:
#     print(" Manfiy son mavjud")

# #Assignment amal
# n = 23
# n *= 5
# n /= 3
# n += 2
# print(n)

# #berilgan sonni bitlarini o'chirish
# n = 29
# print(bin(n))
# print(n>>3)
# print(n&~((1<<3) -1))

# #berilgan matnni list orasida mavjudligin tekshirish
# leg = ["word", "dior", "men", "always", "data"]
# n = input(" Enter the word ")
# if n in leg:
#     print(n, " this word same with list ")
# else:
#     print(n, " this word no same with list ")
#

# #check the list and object same condition
# a = [1, 2, 3]
# b = a
# c = a.copy()
# if a is c:
#     print(" Same lists ")
# else:
#     print(" Not same list")
# print(id(a), id(b), id(c))

# # ikkilik va on oltilik binar ko'rinishi
# n = 123
# print(bin(n), hex(n))

# #string to intager is type change
# a = "15"
# b = "2.5"
# a = int(a)
# b = float(b)
# print(a+b)

# #check length with list len
# list1 = [1, 2, 3]
# list2 = [5, 4, 7, 4, 4, 423]
# if len(list1) == len(list2):
#     print(" Sama length lists ")
# else:
#     print(" It is not same len lists")

# #son ijobiy musbat va toq ekanligiga tekshriish
# n = int(input(" Sonni kiriting "))
# if n>=0 and n%2==1:
#     print(" Son ijobiy musbat va toq son")
# else:
#     print(" Bunday emas")
#

# #uchburchak yuzini hisoblash
# a = 3
# b = 4
# c = 5
# p = (a+b+c)/2
# s = (p*(p-a)*(p-b)*(p-c))**0.5
# print(" Uchburchak yuzi ",s)
# print(64**(1/6))

# #bitwise orqali qiymatlarni almashtirish
# x = 6
# y = 4
# z = 5
# x = x^y^z
# y = x^y^z
# z = x^y^z
# x = x^y^z
#
# print(x, y, z)

# #5 ta o'zgaruvchining kamida beshtasi true bolganini tekshirish
# a = False
# b = False
# c = True
# d = True
# e = False
# count = sum([a, b, c, d ,e])
# result = count >= 3
# print(result)

# #index orqali bir xil element ekanligiga tekshirish
# list1 = [1, 2, [3, 4]]
# list2 = list1.copy()
# if list1[1:2] == list2[1:2]:
#     print(" List elementi teng")
# else:
#     print(" List elementi teng emas")
# print(list1[2][1])

# #ikkilik ko'rinish
# a = 2331
# print(bin(a))
# print(bin(a<<2))
# print(bin(a>>2))
# print(a<<2)
# print(a>>2)

# #nutun ro'yxat
# n = ["1", "2", "3", "4"]
# n = list(map(int, n))
# n = sum(n)
# print(" Elementlar yig'indisi ", n)

# #katta kichik sonni topish
# a = 25
# b = 15
# c = 30
# n = max(a, b, c)
# m = min(a, b , c)
# print(" Max elment ", n, f"\n Min element ", m)
# if a>b:
#     if a>c:
#         print(" Max son ", a)
#     else:
#         print(" max son ", c)
# else:
#     if b>c:
#         print(" Max son ", b)
#     else:
#         print(" max son ", c)

# #elemetlari
# v = [5, 10, 15, 11]
# l = [1, 5, 10, 15, 20]
# r = all(value in l for value in v)
# if v in l:
#     print(" Berilgan qiymat listning elemntlari ")
# else:
#     print(" berilgan qiymat list elmentlari emas")
#
# print(r)

# import re
# #matn ichidagi sonlarni topish
# text = "num1=5, num2=10, num3=15"
# b = ' '.join(char for char in text if char.isnumeric())
# b = b.split()
# print(b)
#
# numbers = list(map(int, re.findall(r'm(\d+)', text)))
# print(sum(numbers))
# shifted_numbers = [num << 2 for num in numbers]
# print("Chapga 2 bit surilgan:", shifted_numbers)


m =  4
print(bin(4))
m <<= 1
print(m, bin(m))