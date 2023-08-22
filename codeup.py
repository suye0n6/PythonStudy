r, g, b = input().split()#3가지 색을 입력받음

r = int(r) #형변환을 시켜줌
g = int(g)
b = int(b)

for i in range(0, r) :
    for j in range(0, g) :
        for k in range(0, b) :
            print(i, j, k)

print(r*g*b)