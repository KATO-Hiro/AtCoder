# -*- coding: utf-8 -*-


def main():
    import sys
    from math import lcm

    input = sys.stdin.readline

    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    candidate = p[0]

    if n >= 2:
        for pi in p[1:]:
            candidate = lcm(candidate, pi)

            if candidate > m:
                break

    if candidate <= m:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
