import random

square_matrix_size = 5

matrix=[[0 for _ in range(square_matrix_size)] for _ in range(square_matrix_size)]

numbers_for_matrix = []

for i in range(square_matrix_size):
    for j in range(square_matrix_size):
        numbers_for_matrix.append(random.randint(0,100))

numbers_for_matrix_index = 0

print("Массив данных для матрицы:")
print(numbers_for_matrix)

for j in range(square_matrix_size):
    if j == 0 or j % 2 == 0:
        for i in range(0,square_matrix_size,1):
            matrix[i][j] = numbers_for_matrix[numbers_for_matrix_index]
            numbers_for_matrix_index = numbers_for_matrix_index + 1
    else:
        for i in range(square_matrix_size-1,-1,-1):
            matrix[i][j] = numbers_for_matrix[numbers_for_matrix_index]
            numbers_for_matrix_index = numbers_for_matrix_index + 1

print()

print("Матрица А: ")

for line in matrix:
    output_string = ""
    for character in line:
        output_string += str(character) + " "
    print(output_string)