n, m = list(map(int, input().split()))
basket= []
for i in range(n):
    basket.append(i + 1)
for _ in range(m):
    i, j = list(map(int, input().split()))
    basket[i-1:j] = basket[i-1:j][::-1]

for i in range(len(basket)):
    print(basket[i], end=" ")