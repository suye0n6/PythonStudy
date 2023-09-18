def count_ways(n, m, lst):
    dp = [0] * (n+1) #동적 
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i >= j:
                dp[i] += dp[i-j]
    return dp[n]

# 입력 받기
n, m = map(int, input().split())
lst = list(map(int, input().split()))

# 계단 오르기 방법의 수 계산
ways = count_ways(n, m, lst)

print(ways)
