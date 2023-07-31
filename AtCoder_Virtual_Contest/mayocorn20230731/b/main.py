# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    count_a = Counter(a)
    count_b = Counter()

    for ci in c:
        count_b[b[ci]] += 1

    ans = 0

    for key, value in count_a.items():
        ans += value * count_b[key]

    print(ans)


if __name__ == "__main__":
    main()
