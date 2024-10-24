while(True):
    lst = [0, 0, 0, 0]
    try:
        str_input = input()
        if str_input == "":
            break
        for s in str_input:
            if s.islower():
                lst[0] += 1
            elif s.isupper():
                lst[1] += 1
            elif s.isdigit():
                lst[2] += 1
            elif s == " ":
                lst[3] += 1

        print(" ".join(map(str, lst))) 
    except EOFError:
        break