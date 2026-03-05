string = input()

result = []
for i in range(1, len(string)-1):
    for j in range(i+1, len(string)):
        part1 = string[:i][::-1]
        part2 = string[i:j][::-1]
        part3 = string[j:][::-1]

        result.append(part1+part2+part3)

print(min(result))