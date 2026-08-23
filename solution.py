rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the adjacency matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

values = []
column_indices = []
row_pointer = [0]

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 0:
            values.append(matrix[i][j])
            column_indices.append(j)

    row_pointer.append(len(values))

print("\nCSR Representation")

print("Values:", values)
print("Column Indices:", column_indices)
print("Row Pointer:", row_pointer)

print("\nReconstructed Graph Information")

for i in range(rows):
    start = row_pointer[i]
    end = row_pointer[i + 1]

    for k in range(start, end):
        j = column_indices[k]
        value = values[k]

        print("Edge:", i, "->", j, "Weight:", value)
