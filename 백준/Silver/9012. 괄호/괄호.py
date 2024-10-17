n = int(input())
for _ in range(n):
    ps = input()
    lCnt = 0
    rCnt = 0
    result = "YES"
    for p in ps:
        if p == "(":
            lCnt += 1
        else:
            rCnt += 1
        if lCnt < rCnt:
            result = "NO"
    if lCnt != rCnt:
        result = "NO"
    print(result)