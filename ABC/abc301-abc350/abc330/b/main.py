# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = list()

    for ai in a:
        if ai <= l:
            ans.append(l)
        elif r <= ai:
            ans.append(r)
        else:
            ans.append(ai)

    print(*ans)


if __name__ == "__main__":
    main()
