"""Дана строка:
String s = “Посмотрите как Рите нравится ритм”;
необходимо вывести индексы начала всех подстрок - “рит”, независимо от регистра.
Для указанной строки ответ будет 6, 15, 29.
"""

s = "Посмотрите как Рите нравится ритм"

# #solution 1
# for w,e in enumerate(s.lower()):
#     try:
#         if e+s[w+1]+s[w+2]=="рит":
#             print(w)
#     except:pass
#
# #solution 2
# print([n for n in range(len(s.lower())) if s.find("рит",n)==n])
#
#solution 3
i=0
k=s.lower()
while i<len(k):


    i=k.find("рит",i)
    if i==-1:
        break
    print(i)
    i+=1
#solution4
# s1 = s.lower()
# ss = 'рит'
# i = (s1.index(ss))
# while i < len(s1):
#     print(s1.index(ss, i))


    # i = s1.index(ss, i + 1)


