#! /usr/bin/python3
#size = int(input("Enter the size of the array"))
#array = [[int(values) for values in input().split(' ')] for i in range(size)]

size = 3
array = [[4, 7, 9], [5, 7, 6], [3, 4, 5]]
sum_left_diagonal, sum_right_diagonal = 0, 0
for i in range(0, size):
    sum_left_diagonal += array[i][i]
    sum_right_diagonal += array[i][size - 1 - i]
    
# print(f"the left diagonal sum {sum_left_diagonal}")
# print(f"the right diagonal sum {sum_right_diagonal}")
print("the left diagonal sum {}".format(sum_left_diagonal))
print("the right diagonal sum {}".format(sum_right_diagonal))

