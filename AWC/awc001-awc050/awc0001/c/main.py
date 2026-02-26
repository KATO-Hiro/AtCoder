# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    d = sorted(list(map(int, input().split())), reverse=True)
    ans = sum(d[k:])
    print(ans)


if __name__ == "__main__":
    main()
