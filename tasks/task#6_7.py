"""
Дан массив:
int[][] array = {{1, 2, 3, 4, 5}, {6, 7, 8, 9}, {-1, -2, -3, -4}, {-5, -6}};
необходимо вывести количество элементов в массиве.
"""
lst=[[1, 2, 3, 4, 5], [6, 7, 8, 9], [-1, -2, -3, -4], [-5, -6]]
elements=0
for i in lst:
    elements=elements+len(i)
print(elements)