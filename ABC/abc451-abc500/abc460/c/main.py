# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    ans = 0

    for ai in a:
        if b and b[-1] <= ai * 2:
            b.pop()
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
