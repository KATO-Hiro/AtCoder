# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    ab = [int(input()) for _ in range(n + m)]
    ab.sort(reverse=True)
    ans = sum(ab[:k])
    print(ans)


if __name__ == "__main__":
    main()
