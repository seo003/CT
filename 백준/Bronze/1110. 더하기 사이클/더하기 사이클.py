n = input()
if len(n) == 1:
    result = "0" + n
else:
    result = n
cycle = 0
while(True):
    newN = int(result[0]) + int(result[1])
    result = result[1] + str(newN % 10)
    cycle += 1

    if int(result) == int(n):
        print(cycle)
        break
