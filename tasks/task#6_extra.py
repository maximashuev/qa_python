"""
Дан массив:
String[][] array = {{“Привет”, “всем”, “кто”}, {“изучает”, “язык”, “программирования”}, {“java”}};
необходимо подсчитать количество строк в массиве, которые не содержат буквы “е”.
"""
lst=[["Привет", "всем", "кто"], ["изучает","язык","программирования"], ["java"]]

output=0
for i in lst:
    for g in i:
        if "е" not in g:
            output+=1
print(output)