n = int(input())

matrix_of_char = []

for _ in range(0, n):
    matrix_of_char.append(list(input()))

symbol = input()
location = ()
found = False

for row in range(0, n):
    if found:
        break
    for col in range(0, n):
        if matrix_of_char[row][col] == symbol:
            location = (row, col)
            found = True

if found:
    print(location)
else:
    print(f"{symbol} does not occur in the matrix")