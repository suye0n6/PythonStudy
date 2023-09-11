n = int(input()) ##바둑판에 올려 놓을 흰 돌 갯수 입력 받기
location = []        ##배열 선언

for i in range(20): #좌표가 1~19까지니까 20까지 배열 돌려주기
    location.append([]) #좌표까지 돌리면서 배열안에 값 삽입하기
    
    for j in range(20): #20까지 배열 돌려주기
        location[i].append(0) #배열 i를 값에 넣어주기

for i in range(n):
    x, y = map(int, input().split()) ##x,y 좌표값 넣어주기
    location[x][y] = 1
    
for i in range(1, 20):
    for j in range(1, 20):
        print(location[i][j], end=" ")
        
    print("")
