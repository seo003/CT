name = input()
num = int(input())
    
baseL = name.count("L")
baseO = name.count("O")
baseV = name.count("V")
baseE = name.count("E")
score_list = {}
for _ in range(num):
    team = input()
    L = baseL + team.count("L")
    O = baseO + team.count("O")
    V = baseV + team.count("V")
    E = baseE + team.count("E")

    score = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    score_list[team] = score

score_list = sorted(score_list.items(), key=lambda x: (-x[1], x[0]))
print(score_list[0][0])