# -*- coding: utf-8 -*-


def main():
    from itertools import permutations

    n = list(input())
    m = len(n)
    patterns = permutations(n)
    ans = 0

    for pattern in patterns:
        for i in range(1, m):
            former = pattern[:i]
            latter = pattern[i:]

            # Verify leading zeros
            former2 = tuple(str(int(''.join(former))))
            latter2 = tuple(str(int(''.join(latter))))

            if len(former) != len(former2):
                continue
            if len(latter) != len(latter2):
                continue

            ans = max(ans, int(''.join(former)) * int(''.join(latter)))

    print(ans)


if __name__ == "__main__":
    main()
