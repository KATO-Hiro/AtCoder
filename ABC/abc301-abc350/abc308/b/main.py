# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    c = list(input().rstrip().split())
    d = [""] + list(input().rstrip().split())
    p = list(map(int, input().split()))
    ans = 0

    for ci in c:
        if ci in d:
            i = d.index(ci)
            ans += p[i]
        else:
            ans += p[0]

    print(ans)


if __name__ == "__main__":
    main()
