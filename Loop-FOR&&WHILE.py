from math import factorial
import random
from os.path import split

# while n>=0:
#     s+=n
#     n-=1
#
# print("Sum valuable ", s)
# while n<=10000000000000:
#     print(n)
#     n+=1
# n = 0
# l="q"
# while True :
#
#     if l=="q":
#         print("Quit done")
#         break
#     else:
#         print(n)
#         n+=1
#
# print("While done last number ", n)

# n = input(" Can you enter the word ")
# l = ['number', 'network', 'back', 'camp', 'index', 'symbol']
# l_i = len(l)
# i = 0
# while i < l_i:
#     if l[i] == n:
#         print("This word found congrotulation ", i)
#         break
#     else:
#         i+=1
# else:
#     print(" You didn't find  any words ")


# for i in range(10, 100, 3):
#     print(i)
#
# n = 10
# while n<100:
#     print(n)
#     n+=3

# # for i in reversed(range(1, 12, 1)):
# #     print(i)
# k = "men. uchun"
# l = "men har doim harakat qilishni hohlayman. qljdqlkwj ldaj lkqaj lka j"
# m = len(l.split())
# print(f"This string {m} words")
# c =0
# for w in l.split():
#     for n in w.strip():
#         c+=1
# print(f" Count {c}")
# b = 1
# for n in l:
#     b+=1
# print(b)


# c = {'name': 'james', 'age': 'older', 'gender': 'male'}
# for n, m in c.items():
#     print(n,m)
#
# print(c.items())
# print(c.keys())
# print(c.values())

# c = ['luck', 'men', 'purpose', 'meaning', 21]
# for n in c:
#     if n == 'luck':
#         print(" You are number one ")
#         break
# else:
#     print(" You are crazy boy ")

# n = list(range(0, 100))
# print(n)
#


# n = [23, 43, 6, 234]
# m = [32, 64, 45, 2]
# for i in n:
#     for x in m:
#         print(i, x)
#     print()
# y = 0
#
# while y<len(n):
#     z = 0
#     while  z<len(m):
#         print(n[y], m[z])
#         z+=1
#     print()
#     y+=1
# i = 0
# while True:
#     print(i)
#     i+=1

# l = list(range(1, 25))
# e = []
# o = []
# for n in l:
#     if n%2==0:
#         e.append(n)
#     else:
#         o.append(n)
#
# print(" Even numbers == ", e)
# print(" Odd numbers == ", o)

# r = int(input('Enter the row number '))
#
# for i in range(1, r+1):
#     print(" " * (r - i), end="")
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print(" ")
#
# for i in range(r, 0, -1):
#     print(" " * (r - i), end="")
#     # r dan 1 gacha teskari loop
#     for j in range(1, i+1):  # Joriy satrda `i` marta chop etish
#         print(i, end=" ")
#     print(" ")  # Har satrda yangi qatorga o'tish
#


# r = int(input('Enter the row number '))
#
# for i in range(1, r+1):
#     print(" " * (r - i), end="")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print(" ")
# for i in range(r-1, 0, -1):
#     print(" " * (r - i), end="")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print(" ")



# r = int(input('Enter the row number '))
#
# for i in range(r, 0, -1):
#     print(" " * (r - i), end="")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print(" ")
# for i in range(2, r+1):
#     print(" " * (r - i), end="")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print(" ")

# r = int(input('Enter the row number '))
#
# for i in range(r):
#     print(" " * (r - i), end="")
#     for j in range(i+1):
#         s = factorial(i)//(factorial(j)*factorial(i-j))
#         print(s, end=" ")
#     print(" ")
#


# r = int(input('Enter the row number '))
#
# for i in range(r):
#     print(" " * (r - i), end="")
#     s = 1
#     for j in range(i+1):
#         # s = factorial(i)//(factorial(j)*factorial(i-j))
#         print(s, end=" ")
#         s = s*(i-j)//(j+1)
#     print(" ")

# n = int(input(" Enter te number "))
# n1 = len(str(n))
# t = n
# s = 0
#
# while t>0:
#     d = t%10
#     s +=d**n1
#     t//=10
#
# if s == n:
#     print(" It is armstrong number ")
# else:
#     print(" It is not  armstrong number try later")

#######TASKS####

# ##1- tsiklidan foydalanib 1 dan 10 gacha bo'lgan sonlarni ekranga chiqaring.
#
# for i in range(1, 11):
#     print(i)
#
# i = 1
# while i<=10:
#     print(i)
#     i+=1

# #2 - 1 dan 20 gacha bo'lgan barcha toq sonlarni chiqarib bering.
# for i in range(1, 21, 2):
#     print(i)
#
# a = []
# b = []
# s = 1
# while s<=20:
#     if s%2==0:
#         a.append(s)
#     else:
#         b.append(s)
#     s+=1
# print("Toq sonlar " ,b)
# print("juft sonlar", a)
# o = 1
# while o<=20:
#     if o%2==0:
#         print(o)
#     o+=1


# ## 4- Foydalanuvchidan 5 ta son kiritishni so'rang va ular o'rtachasini hisoblang.
# i = 1
# s = 0
# print(" Enter the 5 number please ")
# while i<=5:
#     k = int(input())
#     s+=k
#     i+=1
#
# print(" Average number ",s/(i-1))
#

# for i in range(1, 6):
#     print("Python")
# s=0
# while s<=5:
#     print("Python")
#     s+=1


# #1 dan 100 gacha bo'lgan sonlarning yig'indisini toping.
# s = 0
# for i in range(1, 101):
#     s+=i
#
# print(s)
# a = 1
# b = 0
# while a<=100:
#     b+=a
#     a+=1
# print(b)


# ##1 dan 10 gacha bo'lgan sonlarning kvadratlarini ro'yxat shaklida yarating.
# s = []
# for i in range(1, 11):
#     s.append(i**2)
#
# print(s)
#
# a = 1
# b = []
# while a<=10:
#     b.append(a**2)
#     a+=1
# print(b)

##88 - Foydalanuvchidan matn kiritishni so'rang va uning har bir harfini yangi qatorda chiqaring.
#
# n = input(" Enter the string ")
# n = n.strip()
# k = int(len(n))
# for i in n:
#     print(i)
# a = 0
# while a<=k:
#     print(n[a])
#     a+=1

# #99-10 ta Fibonachchi sonlarini hisoblang (while tsiklidan foydalaning).
#
# i = 0
# s = 1
# a = 1
# while a<=10:
#     print(i)
#     l = i+s
#     i = s
#     s = l
#     a+=1

# ### 10 -- 20 dan 1 gacha sonlarni kamayish tartibida chiqaring.
# for i in range(20, 0, -1):
#     print(i)
#
# a = 20
# while a>0:
#     print(a)
#     a-=1


# #11 - Foydalanuvchidan 5 ta son kiritishni so'rang va eng katta va eng kichik sonlarni toping.
# print(" Enter the five number ")
# a = []
# e = []
# for i in range(1, 6):
#     k = int(input())
#     a.append(k)
# print(max(a), min(a))
# b = 1
# while b<=5:
#     f = int(input())
#     e.append(f)
#     b+=1
# print(max(e), min(e))


# ## 12 -- 1 dan 100 gacha bo'lgan barcha polindrom sonlarni chiqarib bering (masalan, 121, 22).
# a = []
# for i in range(1, 111):
#     i = str(i)
#     if i==i[::-1]:
#         a.append(i)
#     i = int(i)
# print(a)

# ##13 -- Foydalanuvchidan o'nlik sonlar (float) kiritishni so'rang va ularning yig'indisini hisoblang. Kiritish "stop" bilan to'xtatiladi.
# s = 0
# print("Enter the 5 float numbers ")
# while True:
#     k = input()
#     if k == 'stop':
#         print("Stop the process")
#         break
#     k = float(k)
#     s += k
# print("Sum float numbers ", s)

# ##14 -- Kompyuter 1 dan 100 gacha tasodifiy son o'ylaydi. Foydalanuvchi uni topishi kerak.
#
# print(" 1 dan 100 gacha bo'lan sonni kiriting ")
# while True:
#     k = int(input())
#     s = random.randint(1,100)
#     print(s)
#     if k == s:
#         print("Sizni tabriklaymiz topdingiz ", k)
#     else:
#         print("Qayta urinib ko'ring " )

# ## 15-- 1 dan 50 gacha bo'lgan barcha oddiy sonlarni chiqarib bering.
#
# for i in range(2, 51):
#     a = True
#     for z in range(2, int(i**0.5)+1):
#         if i%z == 0:
#             a = False
#             break
#     if a:
#         print(i, end=" ")


# ##16-Foydalanuvchidan butun son kiritishni so'rang va uning faktorialini hisoblang.
# n = int(input(" Enter the intager number "))
# i = 1
# s = 1
# while i<=n:
#     s*=i
#     i+=1
# print(s)
# d = 1
# for a in range(1, n+1):
#     d*=a
# print(d)

# ##17 --Foydalanuvchidan butun son kiritishni so'rang va undagi barcha raqamlarning yig'indisini hisoblang.
#
# n = input(" Enter the integer number ")
# n = str(n)
# s = 0
# for i in n:
#     i = int(i)
#     s+=i
# print(s)


# ##18 -- Foydalanuvchidan 5 ta so'z kiritishni so'rang. Bir xil bo'lgan so'zlarning sonini toping.
#
# words = []
# for i in range(5):
#     word = input(f"{i+1} - so'zni kiriting: ")
#     words.append(word)
#
# c = {}
# for word in words:
#     if word in c:
#         c[word]+=1
#     else:
#         c[word] = 1
# for word, c in c.items():
#     print(f'{word}: {c} ta ' )

# ## 19 --1 dan 100 gacha bo'lgan barcha raqamlarni ko'rib chiqib, raqamlari bir xil bo'lganlarni chiqaring (masalan, 11, 22, 33).
# for i in range(11, 101):
#     i = str(i)
#     if i == i[::-1]:
#         print(i)
#     i = int(i)
#
# n = int(input(" Sonni kiriting "))
# for i in range(10, n+1):
#     if len(set(str(i)))==1:
#         print(i)
#
# print(set(str(n)))

# ##22-- foydalanuvchidan matn kiritishni so'rang va uni teskari o'giring.
# n = input(" enter the message for reversing \n")
# print(n[::-1])

# ##23 --Foydalanuvchidan 10 ta son kiritishni so'rang va ularning ichidan juft sonlarni alohida chiqaring.
# print(" Enter the 10 numbers ")
# l = []
# for i in range(1, 11):
#     k = int(input(f"{i}- sonni kiriting : "))
#     if k%2==0:
#         l.append(k)
#
#
# print(l)

# ##24 --5 qatorli raqamlar piramidasini yarating
# n=5
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for y in range(1, i+1):
#         print("0", end=" ")
#     print(" ")
# for i in range(n-1, 0, -1):
#     print(" "*(n-i), end="")
#     for y in range(1, i+1):
#         print("*", end=" ")
#     print(" ")

# # ## 25 -- Foydalanuvchidan matn kiritishni so'rang va har bir harfni keyingi harfga almashtirib kodlang ('abc' -> 'bcd'). bu nima deganing
# #
# # n = input(" Matnni kiriting ")
# #
# # new = ""
# #
# # for i in n:
# #     if i.isalpha():
# #         if i == "m":
# #             new+= "b"
# #         elif i == "e":
# #             new +="a"
# #         else:
# #             new+=chr(ord(i)+1)
# #     else:
# #         new+=i
# # print(new)
# l = []
# for i in range(1, 101):
#     l.append(i)
# print(l)
#
#
# r = input(" Enter the you want to remove numbers \n").split()
# r = [int(i) for i in r]
#
# for i in r:
#     if i in l:
#         l.remove(i)
#
# print(" New list numbers : ", l)


# ##27 -- Kompyuter tasodifiy son o'ylaydi va foydalanuvchi uni 5 urinishda topishi kerak.
#
# l = random.randint(1, 10)
# i = 1
# while i<=5:
#     k = int(input(" Enter the number "))
#     if k == l:
#         print(" Congratulation You are number one " , l)
#     else:
#         print(f"{5-i} left ")
#     i+=1
# else:
#     print(" You are not winner")

# ## 28 -- 1 dan 1000 gacha bo'lgan barcha sonlarning to'qsonlar yig'indisini hisoblang.
# s = 0
# for i in range(1, 11):
#     if i%2==1:
#         s+=i
# print(s)

# ##Foydalanuvchidan bir nechta so'zlarni kiritishni so'rang va ularni alifbo tartibida qaytaring.
#
# n = input(" Enter the words ").split()
# sorted(n)
# l = " ".join(sorted(n))
#
# print(l)

##30 -- complate