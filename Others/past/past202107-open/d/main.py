# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = ["axa", "ixi", "uxu", "exe", "oxo"]
    ans = s
    count = 0

    for patterns in permutations(t):
        u = s

        for pattern in patterns:
            u = u.replace(pattern, "...")

        candidate = u.count(".")

        if candidate > count:
            ans = u
            count = candidate

    print(ans)


if __name__ == "__main__":
    main()
