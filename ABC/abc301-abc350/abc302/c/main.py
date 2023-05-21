# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]

    for pattern in permutations(s):
        count = 0

        for p1, p2 in zip(pattern, pattern[1:]):
            tmp = 0

            for s1, s2 in zip(p1, p2):
                if s1 != s2:
                    tmp += 1

            if tmp == 1:
                count += 1

        if count == n - 1:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
