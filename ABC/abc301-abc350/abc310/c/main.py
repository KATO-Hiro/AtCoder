# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    used = set()
    ans = 0

    for si in s:
        if si not in used:
            ans += 1

        used.add(si)
        used.add(si[::-1])

    print(ans)


if __name__ == "__main__":
    main()
