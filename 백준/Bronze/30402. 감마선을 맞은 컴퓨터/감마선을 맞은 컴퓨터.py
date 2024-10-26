lst = []
for _ in range(15):
    lst.append(input())
result = ""
for l in lst:
    if 'w' in l:
        result = 'chunbae'
    elif 'b' in l:
        result = 'nabi'
    elif 'g' in l:
        result = 'yeongcheol'
print(result)