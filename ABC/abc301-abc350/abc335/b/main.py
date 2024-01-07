# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = list()

    for x in range(n + 1):
        for y in range(n + 1):
            for z in range(n + 1):
                if (x + y + z) <= n:
                    ans.append((x, y, z))

    ans.sort()

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
