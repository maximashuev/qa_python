"""
Дан массив:
int[][] array = {{1, 2, 3, 4, 5}, {6, 7, 8, 9}, {-1, -2, -3, -4}, {-5, -6}};
необходимо вывести максимальное значение массива.
"""
lst=[[1, 2, 3, 4, 5], [6, 7, 8, 9], [-1, -2, -3, -4], [-5, -6]]
#solution 1
max_int=0
for i in lst:
    for g in i:
        if g>max_int:
            max_int=g
print(max_int,"\n")

#solution 2
max_int=[]
for i in lst:
    max_int.append(max(i))

print(max(max_int))