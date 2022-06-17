# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    k = 1
    ans = [[0] * w for _ in range(h)]

    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                a[k - 1] -= 1
                ans[i][j] = k

                if a[k - 1] == 0:
                    k += 1
                
        else:
            for j in range(w - 1, -1, -1):
                a[k - 1] -= 1
                ans[i][j] = k

                if a[k - 1] == 0:
                    k += 1
                    
    for ai in ans:
        print(*ai)


if __name__ == "__main__":
    main()
