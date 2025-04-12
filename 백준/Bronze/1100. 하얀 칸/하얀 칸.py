result = 0
for i in range(8):
    str = input()
    if i%2==0:
        for j in range(8):
            if j%2==0:
                if str[j]=='F':
                    result += 1
    else:
        for j in range(8):
            if j%2==1:
                if str[j]=='F':
                    result += 1
print(result)