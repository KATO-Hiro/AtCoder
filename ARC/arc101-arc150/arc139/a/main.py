# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    ans = -1

    for ti in t:
        candidate = ans >> ti
        candidate += 1

        if candidate % 2 == 0:
            candidate += 1

        candidate <<= ti
        ans = candidate

    print(ans)


if __name__ == "__main__":
    main()
