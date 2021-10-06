# -*- coding: utf-8 -*-


def main():
    from itertools import permutations

    n = list(input())
    m = len(n)
    patterns = permutations(n, m)
    ans = 0

    for pattern in patterns:
        for i in range(1, m):
            former = pattern[:i]
            latter = pattern[i:]

            ans = max(ans, int(''.join(former)) * int(''.join(latter)))

    print(ans)


if __name__ == "__main__":
    main()
