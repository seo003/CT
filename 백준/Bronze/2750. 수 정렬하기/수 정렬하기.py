n = int(input())
input_list = [int(input()) for _ in range(n)]

input_list.sort()

for i in range(n):
    print(input_list[i])