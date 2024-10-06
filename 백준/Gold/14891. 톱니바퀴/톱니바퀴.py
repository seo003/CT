# 시계방향
def right(list, num):
    pole = list[num].pop()
    list[num].insert(0, pole)
    return list

# 반시계방향
def left(list, num):
    pole = list[num].pop(0)
    list[num].append(pole)
    return list

wheels = []
for _ in range(4):
    wheel = input()
    wheels.append(list(wheel))

n = int(input())
turn = []
for _ in range(n):
    key, value = map(int, input().split())
    turn.append([key, value])

# N:0 S:1
# 시계:1 반시계:-1
for num, way in turn:
    num -= 1
    wayList = [0, 0, 0, 0]
    wayList[num] = way

    for i in range(num, 3):
        if wheels[i][2] != wheels[i + 1][6]:
            wayList[i + 1] = -wayList[i]
        else:
            break

    for i in range(num, 0, -1):
        if wheels[i][6] != wheels[i - 1][2]:
            wayList[i - 1] = -wayList[i]
        else:
            break

    for i in range(4):
        if wayList[i] == -1:
            left(wheels, i)
        elif wayList[i] == 1:
            right(wheels, i)
cnt = 0
if wheels[0][0] == '1':
    cnt += 1
if wheels[1][0] == '1':
    cnt += 2
if wheels[2][0] == '1':
    cnt += 4
if wheels[3][0] == '1':
    cnt += 8
print(cnt)