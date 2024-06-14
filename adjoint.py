from matrix import Matrix

print("Welcome, this program finds the adjoint matrix of any 3x3.")

matrix = []
print("Please enter the 3x3 matrix row by row, with each element separated by a space:")
for i in range(3):
    row = input(f"Enter row {i+1}: ").strip().split()
    if len(row) != 3:
        print("Error: Each row must contain exactly 3 elements.")
        break
    matrix.append([int(x) for x in row])


m = Matrix(matrix)

if m.is_valid():
    adj = m.adjoint()
    print("The adjacent is:")
    for row in adj:
        print(row)
else:
    print("invalid matrix try again")

