num=int(input())

def f(num):
    if num!=1:
        f(num-1)
    print(num-1)
f(num)