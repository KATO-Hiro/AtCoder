# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    k = min(k, c[0])
    ans = 0

    for i in range(1, n + 1):
        count = c[i]

        ans += (k - min(k, count)) * i
        k = min(k, count)

        if count == 0:
            print(ans)
            exit()
        
    print(ans)


if __name__ == "__main__":
    main()
