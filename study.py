n = int(input())
p = input().split()

for i in range(n) :
    p[i] = int(p[i]) #리스트 안에 p 값 넣기

d = []
for i in range(24) :
    d.append(0) #d 라는 새로운 리스트를 만들어 24번까지 빈 리스트를 만듬


for i in range(n) :
    d[p[i]] += 1   #번호 호출시 1 플러스

for i in range(1, 24) :
    print(d[i], end=' ') #값을 i 부터 시작해 공백 포함 출력



#역순 출력
n = int(input())
p = input().split()

for i in range(n) :
    p[i] = int(p[i]) #리스트 안에 p 값 넣기

d = []
for i in range(24) :
    d.append(0) #d 라는 새로운 리스트를 만들어 24번까지 빈 리스트를 만듬


for i in range(n) :
    d[p[i]] += 1   #번호 호출시 1 플러스

for i in range(1, 24) :
    print(d[-i], end=' ') #값을 i 부터 시작해 공백 포함 출력