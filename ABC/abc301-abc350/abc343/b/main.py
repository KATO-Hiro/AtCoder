# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        a = list(map(int, input().split()))
        ans = list()

        for i, ai in enumerate(a, 1):
            if ai == 1:
                ans.append(i)

        print(*ans)


if __name__ == "__main__":
    main()
