# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = list()

    for ai in a:
        if ai % k == 0:
            ans.append(ai // k)

    print(*sorted(ans))


if __name__ == "__main__":
    main()
