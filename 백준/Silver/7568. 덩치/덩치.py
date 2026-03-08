num = int(input())
persons = []
result = [1 for _ in range(num)]
for _ in range(num):
    persons.append(list(map(int, input().split())))

for i in range(num-1):
    for j in range(i+1, num):
        if persons[i][0] > persons[j][0]:
            if persons[i][1] > persons[j][1]:
                result[j] += 1
        elif persons[i][0] < persons[j][0]:
            if persons[i][1] < persons[j][1]:
                result[i] += 1
for r in result:
    print(r, end=" ")