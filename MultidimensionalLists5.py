n = int(input())

matrix = [[0] * n for row in range(0, n)]

for x in range(0, n):
    line = list(map(int, input().split()))
    for y in range(0, n):
        matrix[x][y] = line[y]

sum_diagonal = sum(matrix[n - i - 1][n - i - 1] for i in range(n))
print(sum_diagonal)
