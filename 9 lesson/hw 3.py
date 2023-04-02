def COP():
   import os
   a = open("№1.txt")
   b = open ('№2.txt', 'w')
   for i in a != 1:
       print(b)

COP()

# Хотел вывести на экран открытый файл 2 и там отобразить только целые цифры, в твоём и чужом решение выводятся числа,
# но все подряд, целые или целые не учитывается.


# def COP():
#     import os
#     with open("№1.txt") as doc1:
#         with open ("№2-0.txt", "w") as doc2:
#             read1 = doc1.read()
#             for i in read1:
#                 if i != 1:
#                     doc2.write(i)

# COP()


# with open ("№1.txt", "r") as file1:
#     content = file1.read()

#     numbers = " "

#     for i in content:
#         if i.isdigit():
#             numbers += i

#     if numbers:
#         with open("№2-1.txt", "w") as file2:
#             file2.write(numbers)

# import re

# with open("№1.txt", "r") as f1:
#     with open("№2-2.txt", "w") as f2:
#         for i in f1:
#             nums = re.findall(r"\b[1-9][0-9]*\b", i)

#             if nums:
#                 f2.write(" ".join(nums) + "\n")
