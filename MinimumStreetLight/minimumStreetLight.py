def Sort_Tuple(tup):
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


def solve(l, n):
    rang = [[0, 0] for i in range(n)]
    # print(rang)
    for i in range(n):
        id = i + 1
        rang[i][0] = max(1, id - l[i])
        rang[i][1] = min(n, id + l[i])

    Sort_Tuple((rang))

    i = 0
    ans = 0
    while i < n:
        p = rang[i]
        ans += 1
        while (i + 1 < n):
            if (rang[i][0] != rang[i + 1][0]):
                break
            p[1] = max(p[1], rang[i + 1][1])
            i += 1
        while (i < n):
            if rang[i][1] > p[1]:
                break
            i += 1

    return ans


n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(solve(l, n))