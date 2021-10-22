inps = []
ans = []
for i in range(int(input())):
    inps.append(list(map(lambda x: int(x), input().split(' '))))
for n in inps:
    if not n[0] % 2:
        if n[0] == n[1]:
            ans.append(n[0] * 2)
        elif n[1] == n[0] - 2:
            ans.append((n[0] * 2) - 2)
        else:
            ans.append('No Number')
    else:
        if n[0] == n[1]:
            ans.append((n[0] * 2) - 1)
        elif n[1] == n[0] - 2:
            ans.append(((n[0] * 2) - 1) - 2)
        else:
            ans.append('No Number')
for v in ans:
    print(v)