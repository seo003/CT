n = int(input())
result = 0
for _ in range(n):
    word = input()
    abList = []
    for w in word:
        if len(abList) == 0:
            abList.append(w)
        else:
            if abList[-1] == w:
                abList.pop()
            else:
                abList.append(w)
    if len(abList) == 0:
        result += 1

print(result)