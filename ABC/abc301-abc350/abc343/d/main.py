# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, t = map(int, input().split())
    scores = [0] * n
    count = defaultdict(int)
    count[0] = n
    ans = 1

    for _ in range(t):
        ai, bi = map(int, input().split())
        ai -= 1

        count[scores[ai]] -= 1

        if count[scores[ai]] == 0:
            ans -= 1

        scores[ai] += bi
        count[scores[ai]] += 1

        if count[scores[ai]] == 1:
            ans += 1

        print(ans)


if __name__ == "__main__":
    main()
