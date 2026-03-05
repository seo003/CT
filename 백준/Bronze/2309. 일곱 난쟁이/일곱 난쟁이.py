import sys
height = []

for i in range(9):
    height.append(int(input()))
total = sum(height)

height.sort()

for i in range(9):
    for j in range(i+1, 9):
        if total-height[i]-height[j] == 100:
            for k in range(9):
                if k!=i and k!=j:
                    print(height[k])
            sys.exit()