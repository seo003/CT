n = int(input())
sumList = []
for _ in range(n):
    num = int(input())
    if num == 0:
        sumList.pop()
    else:
        sumList.append(num)
print(sum(sumList))