a = int(input())

pi1 = 1
pi2 = 1
tmp = 0

if a >= 3:
    for i in range(a-2):
        tmp = pi2
        pi2 = pi1 + pi2
        pi1 = tmp
print(pi2)