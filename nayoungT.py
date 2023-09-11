n = int(input())
nrr=[list(map(int,input().split()))  for _ in range(n)]
graph=[[0 for _ in range(20)] for _ in range(20)]
for i in nrr:
    for x,y in i:
