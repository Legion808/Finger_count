# import re
#
# a = input(" Enter the password  ")
# b = len(a)
# c = False
#
# while True:
#     if b<7 or b>20: break
#     elif not re.search("[A-Z]", a): break
#     elif not re.search("[a-z]", a): break
#     elif not re.search("[0-9]", a): break
#     elif not re.search("[$#@!]", a): break
#     elif re.search(" ", a): break
#     else:
#         c = True
#         break
# if c:
#     print(" Good combination password ")
# else:
#     print("Password is invalid ")


# a = input(" Enter the string ")
# b = list(a.lower())
#
# if a == a[::-1]:
#     print(" The string is a palindrome ")
# else:
#     print(" This string is not palindrome ")


# a = int(input(" Enter the first number "))
# b = int(input(" Enter the second number "))
#
# if a>b:
#     s = b
# else:
#     s = a
#
# for i in range(1, s+1):
#     if a%i==0 and b%i==0:
#         n = i
#
# print(f" HFC number for {a} and {b} :  ", n)


n = float(input(" Enter the float number"))
print(round(n, 3))
print(n.__ceil__())