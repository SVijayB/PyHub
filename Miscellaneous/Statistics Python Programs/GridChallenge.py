n=int(input())
for _ in range(n):
    arr=(sorted(input()) for _ in range((int(input()))))
    idx=(True if (list(z)==sorted(z)) else False for z in zip(*arr))
    print(['NO','YES'][all(idx)])

