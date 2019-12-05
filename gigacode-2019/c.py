# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    d = int(input())
    a = list(accumulate(list(map(int, input().split()))))
    b = list(map(int, input().split()))
    ans = float('inf')

    for ai, bi in zip(a, b):
        if ai >= bi:
            ans = min(ans, bi)

    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
