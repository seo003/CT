tc = int(input())

for _ in range(tc):
    scores = list(map(int, input().split()))
    old = sum(scores) - max(scores) - min(scores)
    oldScores = scores.copy()
    oldScores.remove(max(scores))
    oldScores.remove(min(scores))
    
    if max(oldScores)-min(oldScores) >= 4:
        print("KIN")
    else:
        print(old)