"""
Дан массив:

int[][] array = {{1, 2, 3, 4, 5}, {6, 7, 8, 9}, {-1, -2, -3, -4}, {-5, -6}};

необходимо вывести сумму элементов массива.
"""
lst=[[1, 2, 3, 4, 5], [6, 7, 8, 9], [-1, -2, -3, -4], [-5, -6]]
#solution 1
output=[]
for i in lst:
    output.append(sum(i))
print("solution 1","\n",sum(output),"\n")

#solution 2
output2=0
for i in lst:
    output2= output2 + sum(i)
print("solution 2","\n",output2)


