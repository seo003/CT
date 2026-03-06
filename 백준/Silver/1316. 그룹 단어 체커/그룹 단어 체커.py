num = int(input())
result = 0

for _ in range(num):
    string = input()
    stack = []
    for i in range(len(string)):
        if string[i] not in stack: 
            stack.append(string[i]) 
        elif string[i] != string[i-1]:
            break
    else:
        result += 1
print(result)