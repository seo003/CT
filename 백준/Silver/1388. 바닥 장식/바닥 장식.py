n, m = list(map(int, input().split()))
rooms = []
result = 0
for _ in range(n):
    rooms.append(list(input()))

for i in range(n):
    for j in range(m):
        if rooms[i][j] == "-":
            if j < m - 1 and rooms[i][j] != rooms[i][j + 1]:
                result += 1
            if j == m-1: result += 1
        else:
            if i < n - 1 and rooms[i][j] != rooms[i + 1][j]:
                result += 1
            if i==n-1: result += 1

print(result)