# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        ai = a[i]

        for j in range(i, n):
            ai = min(ai, a[j])
            ans = max(ans, ai * (j - i + 1))
    
    print(ans)


if __name__ == "__main__":
    main()
