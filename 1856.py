# 'deep'이라는 재귀 함수를 정의 이 함수는 정수 'n'을 입력
def deep(n):
    # 기본 경우 만약 n이 1보다 작으면, 0을 반환
    if (n<1):
        return 0
    # 기본 경우 만약 n이 1과 같다면, 1을 반환
    elif (n==1):
        return 1
    else:
        # 재귀 단계 n-1, n-2, n-3을 인자로 갖고 재귀적으로 호출한 결과를 더하기
        return deep(n-1) + deep(n-2) + deep(n-3)

# 사용자로부터 'n' 값을 입력
n = int(input())

# 'deep' 함수를 'n+1'을 인자로 호출하고, 결과를 'answer'에 넣어줌
answer = deep(n+1)

# 'answer'의 값을 출력
print(answer)
