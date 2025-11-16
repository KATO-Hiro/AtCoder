# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    x = list(input().rstrip())
    ans = 10**18

    for pattern in permutations(x):
        if pattern[0] == "0":
            continue

        candidate = int("".join(pattern))
        ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
