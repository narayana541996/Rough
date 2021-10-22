def rev(n):
    s = 0
    if n > 9:
        while n:
            r = n % 10
            n = n // 10
            s = (s*10) + r
    else:
        s = n
    return s
#print(rev(138))

nums = []
for i in range(int(input(''))):
    nums.append(list(map(lambda x: int(x), input('').split(' '))))

sums = []
for num in nums:
    sums.append(rev(rev(num[0]) + rev(num[1])))
print(sums)