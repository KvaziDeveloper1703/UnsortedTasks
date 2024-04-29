import random

N = 5
M = 5

matrix=[[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        matrix[i][j] = random.randint(0,100)

print("Матрица А: ")

for line in matrix:
    output_string = ""
    for character in line:
        output_string += str(character) + " "
    print(output_string)

number_of_rows_in_matrix = len(matrix)

for i in range(number_of_rows_in_matrix // 2):
    matrix[i], matrix[number_of_rows_in_matrix-i-1] = matrix[number_of_rows_in_matrix-i-1], matrix[i]

print("Матрица B: ")

for line in matrix:
    output_string = ""
    for character in line:
        output_string += str(character) + " "
    print(output_string)