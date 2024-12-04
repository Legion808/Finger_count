# name = "Behruz"
# lan =" python"
# num: int = 4
# print(num)
# n = 13.24
# print("My name is "f"{name.lower()}")
# print(name[::2])
# print(" I need to learn "f"\"lan\"")
# print(f"I always {int(n**2)} try \n ")
# print(name.upper()[2])
#
# nume = int(input(" Check "))
#
# print(nume)
#
#
# remove something from the string
#
# s = "You can imagine reality#".strip('#')
#
# print(s)
#
# text = "#!?Salom, Dunyo!?#!"
# cleaned_text = text.strip("#!?")
# print(cleaned_text)  # Natija: "Salom, Dunyo"
#
#
# teskari satr
#
# back = " I always try to improve my life "
# back = back[::-1]
# print(back)
#
#
# satrni katta va kichik harflarda chiqarish
#
# num = " sen3 nega har doim o'rganasan "
# so = "men"
# print(num.upper())
# print(num[::3].lower())
# # print(search(so,""))
# print(len(so))
#
# print(num.count(('a')))
#
# #unli harflarni sonini topish
# ol = "aeiouAEIOU"
# h = input("Satrni kiriting ")
# i = 0
# for char in h:
#     if char in ol:
#         i+=1
# print(i)
#
# #polidromlikni tekshirish
#
# men = input(" Matnni kiriting  ")
# men1 =men[::-1]
# if men==men1:
#     print(" Polidrom message ")
# else: print(" Isn't Polidrom ")
#
# sub stringni ajratib olish
#
# k = " Men har doim harakatdaman "
#
# # print(k.title())
# print(k.replace("a", "1"))
#
# noyob charakterni topish hisoblash
#
# men = input(" Matnni kiriting  ")
# print(len(set(men)))
#
# #anogram yani uzunlik va satr bir xil ekanligiga tekshirish
#
# a = input(" 1 - Satrni kiriting  ")
# b = input(" 2 - Satrni kiriting  ")
#
# if len(a)==len(b) and a==b:
#     print(" anogram string ")
# else: print(" anogram string emas ")
#
#
#
# #berilgan stringdan belgini tanlab olib uni katta qilish
# s = "HAkfHH"
# kk = s[:3]+s[4].lower()+s[5:]
# print(kk)
#
# string uchun eng uzun so'zni topish
#
# men = input(" Enter the string ")
#
# print(k)
#
#
# s = "learrrning"
# b = "Python programming language learning"
# word = s.split()
# maxx = max(word, key=len)
# print(maxx)
#
#
# s = " Qanday Kurra sen nega har doim"
# sen = set()
# res = " "
# for char in s:
#     if char not in sen:
#         res+=char
#         sen.add(char)
#
# print(" Natija ", res)
#
#
# har bir belgi qancha qatnashgani
#
# men = input(" Satrni kiriitng  ")
# sen = set()
# count =0
# for char in men:
#      if char in sen:
#          count+=1
# print(char, count)
#
#
# caesar shifrlash ya'ni 3 ta belgi oldinga surib shifrlash
#
#
#
# s = "325325/523532"
# b = eval(s) # eval string ni to'g'ridan to'g'ri amal qilib bajaradi agar qandaydir amal yozilgan bo'lsa
# print(b)
#
# cut = " You can imagine#any challanges in#your#life! ".rsplit("#", 2)
# print(cut)
#
# #join method
#
# s = ["L","e","s","s","o","n"]
# print("".join(s))
#
# l = "men har doim senga yordam beraman "
# print("".join(s))
# print(l.replace("doim", "kechasi"))
# print(l.capitalize())
# print(l.isupper())
#
# m = "justabit@424.com"
# print(m.isupper())
#
# #isalpha, isnumeric, isalnum
# m = "24324234"
# print(m.isnumeric())
#
# m = "2432423fjawqdqwd@#@4"
# print(m.isalnum())
#
#
# f = " men uni ko'rib men deb yubordim deb o'ylagan men ".count("deb", 1, 25)
# print(f)
#
# a = " men uni ko'rib men deb yubordim deb o'ylagan men ".rfind("yubordim",1,28)
# print(a)
#
# d = " can you help me with money ".rindex("with" ,1, 40)
# print(d)
#
# #111 har bir so'zni bosh harf bilan boshlash
#
# b = input(" Matnni kiriitng  ").title()
# print(b)
#
# #222 katta harflarni kichik kichik harflarni katta qilish
#
# n = input(" How can I help you ?   ").swapcase()
# print(n)
#
# #333 matnni teskari aylantirish
#
# n = input(" Do you wanna drink coffee ")
# print(n[::-1])
#
# #444 matnda nechta belgilangan harf yoki belgi borligini tekshirish
#
# n = " Nega sen har doim harakatdasan "
#
# print(n.find("sen1"))
# print(n.count("a"))
#
# #555 o'rin almashtirish
#
# n = input(" Malumot bering  ")
# print(n.replace("kelajak", " bugun"))
#
# #666 matn boshidagi va oxiridagi bosh joylarni olib tashlash
#
# n = " salom bratan qandaysiz1"
# print(n.strip(" sa z1"))
#
# # 777 so'zni tekshirish
#
# n = "I am trying to learn python information for improve my performance"
# print(n.count("trying"))
#
# #888 mattnni qismlarga jaratish
#
# n = " Hello world "
# print(n.split())
# print(n.split("l"))
#
# #999 katta kichik
#
# n = "Men seni kecha kordim "
# print(n.upper())
# print(n.lower())
# print(n[2].upper())
# print(n[6].lower())
#
#
# print(n[:2].upper()+n[3:].lower())
#
# #listdagi so'zlarni birlashtirish
#
# n = ["back", "hello", "norm"]
#
# print(" ".join(n))
#
# #1111 birinchi va oxirgi harfni olish
# n = "Nega men harkat qilaman"
# n = n.split()
# word1 = []
# for word in n:
#     if len(word)>1:
#         word1.append((word[0], word[-1]))
#     elif len(word)==1:
#         word1.append((word[0], word[0]))
#
# word2 = [(word[0], word[-1]) for word in n]
#
# print(" Sozlarning birinchi va oxirgi harflari", word2)
#
# #1122 ikki matnni teng ekanligiga tekshirish
#
# n = input(" Enter the data ")
# m = input(" Enter the second data ")
#
# if n==m :
#     print(" Same strings ")
# else:
#     print(" It isn't same strings")
#
#
# #1133 matndan keraksiz belgilarni olib tashlash
#
# n = input(" Hello , I am Behruz. How can I help you? ")
#
# clean = "".join(char for char in n if char.isalnum() or char.isspace())
# clean1 = re.sub(r'[^A-Za-z0-9\s]', '', n)
# print(clean)
# print(clean1)
#
#
# #1144 eng uzun so'zni aniqlash
#
# n = input(" Qaysi davlatga borishni hohlaysiz ")
# n=n.split()
# m = max(n, key=len)
# print(m)
#
# #1155 raqamlarni ajratib olish
#
# n = input(" Matnni kiriitng ")
# number = "".join(char for char in n if char.isnumeric() or char.isspace())
# print(number.split())
#
# #1166 space larni qisqartirish
#
# n = input(" salom qalaysiz  ")
# n = n.split()
# print("".join(n))
#
# #1177 harflarning katta kichikligiga qaramay izlash
#
# n = input(" Hello bro! whats up ")
# m = input(" qirilgan soz ")
# if  m.lower() in n.lower():
#     print(f" {m} soz matnda berilgan ")
# else:
#     print(f" {m} soz matnda berilmagan ")
#
# #1188 matndagi sozlarni alfabit boyicha saralash
#
# n = input(" Salom, kuningiz qanday bo'ldi ")
# n = n.split()
# m = " ".join(sorted(n)) 
# print(" saralangan sozlar ", m)
# m1 = sorted(n)
#
# #ikki so'z anoligligiga tekshirish
#
# n = input(" analoglik tekshirish word1 ")
# m = input(" analoglik tekshirish word2 ")
#
# if n==m[::-1]:
#     print(" anolig string")
# else:
#     print(" anolig string emas")
#

# n = "473+432/324-1234"
# print(eval(n))