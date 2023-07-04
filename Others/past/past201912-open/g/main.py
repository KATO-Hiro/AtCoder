# -*- coding: utf-8 -*-


def get_pairs(group):
    from itertools import combinations

    pairs = list()

    for p1, p2 in combinations(group, 2):
        if p1 > p2:
            continue

        pairs.append((p1, p2))

    return pairs


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    a = list()

    for i in range(n):
        ai = [0] * (i + 1) + list(map(int, input().split()))
        a.append(ai)

    groups = product(range(3), repeat=n)
    ans = -(10**18)

    for group in groups:
        group_one = list()
        group_two = list()
        group_three = list()

        for i, g in enumerate(group):
            if g == 0:
                group_one.append(i)
            elif g == 1:
                group_two.append(i)
            else:
                group_three.append(i)

        pairs = get_pairs(group_one)
        pairs += get_pairs(group_two)
        pairs += get_pairs(group_three)
        candidate = 0

        for p1, p2 in pairs:
            candidate += a[p1][p2]

        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
