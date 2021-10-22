n = int(input())
f = n
n = n - 1
while n:
	f *= n
	n -= 1
print(f)