if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [input() for i in range(n)]
    k = int(input())

    for ans in sorted(arr, key = lambda ans: int(ans.split()[k])):
        print(ans)