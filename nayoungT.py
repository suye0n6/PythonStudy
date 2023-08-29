n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])

d = k[0]

for i in range(0, n):
    if d > k[i]:
        d = k[i]
        
print(d)