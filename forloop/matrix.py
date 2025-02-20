# Taking input for the first matrix
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []  # Empty list to store the first matrix
for i in range(rows):
    val = []  # Reset val for each new row
    for j in range(columns):
        val.append(int(input("Enter the value for position (%d, %d): " % (i, j))))
    matrix.append(val)  # Add the row to the matrix

print("First Matrix:", matrix)  # Print the first matrix

# Taking input for the second matrix
matrix1 = []  # Empty list to store the second matrix
for i in range(rows):
    val = []  # Reset val for each new row
    for j in range(columns):
        val.append(int(input("Enter the value for position (%d, %d): " % (i, j))))
    matrix1.append(val)  # Add the row to the matrix

print("Second Matrix:", matrix1)  # Print the second matrix

# Computing the sum of the two matrices
sum_matrix = []  # Empty list to store the sum matrix
for i in range(rows):
    val = []  # Reset val for each new row
    for j in range(columns):
        val.append(matrix[i][j] + matrix1[i][j])  # Adding corresponding elements
    sum_matrix.append(val)  # Add the row to the sum matrix

# Printing the final summed matrix
print("Sum of the two matrices:", sum_matrix)
