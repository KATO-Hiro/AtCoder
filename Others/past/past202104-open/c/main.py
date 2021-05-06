# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list()

    for i in range(n):
        ka = list(map(int, input().split()))
        a.append(ka[1:])

    _, q = map(int, input().split())
    b = list(map(int, input().split()))

    ans = 0

    for ai in a:
        count = 0

        for bi in b:
            if bi in ai:
                count += 1

        if count >= q:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
