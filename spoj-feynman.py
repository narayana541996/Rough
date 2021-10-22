inp = [True]
while inp[-1]:
    inp.append(int(input()))
del(inp[0])
inp.pop()
#print(inp)
for s in inp:
    if s == 0:
        print('')
    elif s == 1:
        print(1)
    else:
        sum = 0
        while s:
            sum += s**2
            s -= 1
        print(sum)