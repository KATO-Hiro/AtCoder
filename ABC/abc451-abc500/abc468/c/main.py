# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    n -= 1
    p = list(map(lambda x: int(x) - 1, input().split()))
    q = list(map(lambda x: int(x) - 1, input().split()))
    p2 = int("".join(map(str, p)))
    q2 = int("".join(map(str, q)))

    ans = 0

    for pattern in permutations(range(n + 1)):
        candidate = int("".join(list(map(str, pattern))))

        if p2 < candidate < q2:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
