# 학생 수 입력 받기
n = int(input())

# 성적 리스트 입력 받기
scores = list(map(int, input().split()))

# 각 학생의 순위를 저장할 리스트 초기화
ranks = [1] * n

# 성적을 기준으로 순위 매기기
for i in range(n):
    for j in range(n):
        if scores[i] < scores[j]:
            ranks[i] += 1
# 결과 출력
for i in range(n):
    print(scores[i],ranks[i])
