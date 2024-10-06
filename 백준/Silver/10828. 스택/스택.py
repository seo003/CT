def isStackNull(stack):
    return len(stack) == 0

n = int(input())
commands = []

for _ in range(n):
    command_input = input().split()
    if command_input[0] == 'push':
        command, value = command_input[0], command_input[1]
    else:
        command, value = command_input[0], None
    commands.append([command, value])

stack = []
for com in commands:
    if com[0] == 'push':
        stack.append(com[1]) 

    elif com[0] == 'pop':
        if isStackNull(stack):
            print("-1")
        else:
            print(stack.pop())  

    elif com[0] == 'size':
        print(len(stack))

    elif com[0] == 'empty':
        if isStackNull(stack):
            print("1")
        else:
            print("0")

    elif com[0] == 'top':
        if isStackNull(stack):
            print("-1")
        else:
            print(stack[-1]) 
