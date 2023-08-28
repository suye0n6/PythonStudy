n = int(input())
p = input().split()

for i in range(n) :
    p[i] = int(p[i])

d = []
for i in range(24) :
    d.append(0)

for i in range(n) :
    d[p[i]] += 1

for i in range(1, 24) :
    print(d[i], end=' ')