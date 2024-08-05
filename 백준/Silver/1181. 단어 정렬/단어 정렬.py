n = int(input())
str_list = [input() for _ in range(n)]
str_list.sort(key=lambda x: (len(x), x))
i = 0
while i < len(str_list)-1:
    if str_list[i] == str_list[i+1]:
        str_list.pop(i+1)
    else:
        i += 1
for p in range(len(str_list)):
    print(str_list[p])
