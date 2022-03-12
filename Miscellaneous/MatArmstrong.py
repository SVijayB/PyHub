def CheckArmstrongNumber(mat, m, n):
    sum_of_diagonal = sum(mat[i][i] for i in range(m))

    res = 0
    temp = sum_of_diagonal
    while temp > 0:
        digit = temp % 10
        res += digit**3
        temp //= 10

    if sum_of_diagonal == res:
        print(sum_of_diagonal)
    else:
        print("0")


# Input
m = int(input())
n = int(input())

# Read matrix
mat = []
for i in range(m):
    row = list(map(int, input().split()))
    mat.append(row)
CheckArmstrongNumber(mat, m, n)
