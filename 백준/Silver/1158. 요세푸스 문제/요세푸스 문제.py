n, k = list(map(int, input().split()))
lst = []
result = []
for i in range(n):
    lst.append(i+1)
order = 0
while lst:
    order += k-1
    order %= len(lst)
    result.append(lst.pop(order))

print("<"+", ".join(map(str,result))+">")