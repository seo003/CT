while(True):
    str = input()
    result = 0
    if str == '#':
        break
    for s in str:
        if s.lower() in ['a','e','i','o','u']:
            result += 1
    print(result)
