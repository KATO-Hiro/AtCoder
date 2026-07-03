# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    s = input().rstrip()
    pos = 0
    ans = 0

    for si in s:
        if si == "R":
            pos += 1
        else:
            pos -= 1

        pos %= n
        ans += a[pos]

    print(ans)


if __name__ == "__main__":
    main()
