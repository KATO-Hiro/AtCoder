# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, h, x = map(int, input().split())
    p = list(map(int, input().split()))
    q = [pi + h for pi in p]
    ans = -1
    value = 10**18

    for i, qi in enumerate(q, 1):
        if qi >= x:
            if qi < value:
                ans = i
                value = qi

    print(ans)


if __name__ == "__main__":
    main()
