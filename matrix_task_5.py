import random

square_matrix_size = 6

matrix=[[0 for _ in range(square_matrix_size)] for _ in range(square_matrix_size)]

for i in range(square_matrix_size):
    for j in range(square_matrix_size):
        matrix[i][j] = random.randint(10,99)

for i in range(square_matrix_size):
    for j in range(square_matrix_size):
        if j > i:
            matrix[i][j] = 0

print("Матрица А: ")

for line in matrix:
    output_string = ""
    for character in line:
        output_string += str(character) + " "
    print(output_string)