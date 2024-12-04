# print(" Hello world")
# n = 11
# m = 45
# sum = n+m
# print(" Ikki  kiritilgan son yig'indis ", sum)
#

##ismini ekranga chiqarish
# name = input("Ismingizni kirirting")
# print(name)


# #Kvadrat yuzini hisoblash
# a = 8
# s = pow(a,3)
# print('Kavadrat yuzi hisoblandi  ',s)

# #kiritilgan sonni ikkiga ko'paytirib chiqarish
# print(85*3)
# number = int(input(" Can you enter the number please! "))
# number = number * 2
# print(number)

# #selsiydan Farangeytga o'tish
#
# sels = float(input(" Iltimos hozirgi selsiy haroratni kiriting"))
# F = sels*(9/5)+35
#
# print(' Farangeyt harorat ' , F)
#


## ikki sonni bir biri bilan almashtirish yoki ko'p sonlarni
# a = 45
# b = 56
# c = 32
# d = 543.3
# # a, b = b, a
# # c = a
# # a = b
# # b = c
# # a = a ^ b
# # b = a ^ b
# # a = a ^ b
# a, b, c, d = d, c, b, a
# print(a,b, c, d)


# #Toq yoki juft sonni topish
# num = int(input(" Can you enter the number "))
# # if (num%2==0):
# #     print(" Bu son Juft" ,num)
# #
# # else:
# #     print(" Bu son Toq", num)
#
# num = ["Juft", "Toq"][num % 2]
# print(num)

# # Ucburcha yuzini hisoblash asos va balandlik
#
# a = float(input(" uchburchak asosini kiiritng  "))
# b = float(input(" uchburchak balandligini kiiritng  "))
# S = (a*b)/2
# print(" Uchburchak yuzi ", S)

# # hafta kunlari sonini kiritish bilan hafta kuni nomi
#
# h = int(input(" Hafta kuni sonini kiriting "))
# if(h==1):
#     print(" Dushanba kuni ")
# elif(h==2):
#     print(" Seshanba kuni ")
# elif(h==3):
#     print(" Choranba kuni ")
# elif(h==4):
#     print(" Payshanba kuni ")
# elif(h==5):
#     print(" Juma kuni ")
# elif(h==6):
#     print(" Shanba kuni ")
# else:
#     print(" Yakshanba kuni")
#
#
# kun = ["Dushanba", "Seshanba","Choranba", "Payshanba", "Juma", "Shanba", "Yakshanba" ]
#
# son = int(input(" 1 dan 7 tagacha sonlarni kiriting "))
#
# result = kun[son-1] if 1 <= son <= 7 else "Noto'gri son kiritdingiz "
#
# print(result)

#
# #sonnig darajasiga oshirish
#
# a = float(input(" Sonnig darajasini kiritng  "))
# b = float(input(" Sonni kiriting  "))
#
# # s = b**a
# s = pow(b,a)
# print(s)

# #1 dan n gacha sonlar yig'indisi
# s = 0
# n = int(input(" N sonini kiriting  "))
#
# # s = (n+1)*n//2
# # for i in range(1, n+1):
# #     s+=i
# #
# s = sum(range(1, n+1))
# print(s)
#

# # 3 xonali son raqamlari yig'indisi
#
# n = int(input(" 3 xonali sonni kiriting  "))
# # n1 = n // 100
# # n2 = (n//10)%10
# # n3 = n%10
# # s = sum(int(v) for v in n)
# son = 0
# while n > 0:
#     son+=n%10
#     n=n//10
#
#
# print(" raqamlar yig'indisi ", son)

# # uchburchakni teng tomonlikka tekshirish
#
# n = int(input(" Uchburchak tomonlarini kiriting   "))
# a = int(input())
# b = int(input())
#
# if n==a and a==b and b==n:
#     print(" Uchburchak teng tomonli  ")
# else:
#     print(" Teng tomonli emas  ")
#

#
# #sonlar ko'paytmasi
#
# a = float(input(" Ikkita sonni kiriting  "))
# b = float(input())
# print(a*b)


# #musbat yoki manfiyligini aniqlash
#
# a = float(input("  Sonni kiriting  "))
# # if a>=0:
# #     print(" Bu musbat son " , a)
# # else:
# #     print(" Bu manfiy son ", a)
# man = " musbat son " if a>=0 else "manfiy son"
# print(man)
#
# #Doira uzunligini hisoblash
#
# a = float(input(" Doira radiusini kiriitng   "))
# l= 2**a
# print(" Doira uzunligi  ", l)

#uch sonning eng kattasi

a = float(input(" Uch sonni kiriting  "))
b = float(input())
c = float(input())

if a>b:
    if a>c:
        print(" katta son ", a)
    else:
        print(" katta son ", c)
elif b>c:
    if b>a:
       print(" katta son ", b)
    else:
        print(" katta son ", a)
else:
    print(" katta son ", c)
#
# n = max(a,b,c)
# print(n)
