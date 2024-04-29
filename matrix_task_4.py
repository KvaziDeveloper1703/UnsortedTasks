matrix=[[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    input_string = input()
    input_data = input_string.split()
    for j in range(4):
        matrix[i][j] = int(input_data[j])

array_of_matrix_values = []

for i in range(4):
    for j in range(4):
        array_of_matrix_values.append(matrix[i][j])

average = sum(array_of_matrix_values) / len(array_of_matrix_values)

for i in range(4):
    for j in range(4):
        if matrix[i][j]<average:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1

print("Матрица А: ")

for line in matrix:
    output_string = ""
    for character in line:
        output_string += str(character) + " "
    print(output_string)