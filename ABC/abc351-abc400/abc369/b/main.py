# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    b = [tuple(input().rstrip().split()) for _ in range(n)]
    ans = 10**9

    for left in range(1, 100 + 1):
        for right in range(1, 100 + 1):
            candidate = 0
            prev_left, prev_right = left, right

            for ai, si in b:
                ai = int(ai)

                if si == "L":
                    candidate += abs(ai - prev_left)
                    prev_left = ai
                else:
                    candidate += abs(ai - prev_right)
                    prev_right = ai

            ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
