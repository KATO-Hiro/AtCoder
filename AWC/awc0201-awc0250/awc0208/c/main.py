# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    v = list(map(int, input().split()))
    v.sort(reverse=True)
    ans = sum(v[::m])
    print(ans)


if __name__ == "__main__":
    main()
