"""It computes individual and cumulative binomial probabilities """


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def comb(n, x):
    return fact(n) / fact(x) * fact(n - x)


def bino(x, n, p):
    return comb(n, r) * p ** x * (p - 1) ** (n - 1)


l, r = list(map(float, input().split(" ")))
odds = l / r
print("{:.3f}".format(sum([bino(i, 6, odds / 1 + odds) for i in range(3, 7)])))
