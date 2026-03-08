n, m = list(map(int, input().split()))
put = [input() for _ in range(n)]

change = {
    '.':'.',
    'O':'O',
    '-':'|',
    '|':'-',
    '/':'\\',
    '\\':'/',
    '^':'<',
    '<':'v',
    'v':'>',
    '>':'^'
}

for j in range(m-1, -1, -1):
    for i in range(n):
        print(change[put[i][j]], end='')
    print()