"""Необходимо вывести все числа кратные 4 между числами 40 и 60 включительно.
Реализовать 2 варианта:
использовать конструкцию if для определения кратности (цикл с шагом 1, i = i + 1);
без использования конструкции if (шаг цикла на ваше усмотрение).
"""
for i in range(40, 61) :
    if i%4==0:
        print(i)

for i in range(40,61,4):
    print(i)
#
# print(40//3)

# for i in range(100,200):
#     if i%7 ==0: #Если число кратно 7
#         print(i) #то, вывести его