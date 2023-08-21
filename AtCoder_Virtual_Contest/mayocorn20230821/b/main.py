# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)
    count = defaultdict(list)

    for _ in range(n):
        si = input().rstrip()
        d[si] += 1

    for key, value in d.items():
        count[value].append(key)

    key_max = max(count.keys())
    # print(count)
    # print(key_max)

    print(*sorted(count[key_max]), sep="\n")


if __name__ == "__main__":
    main()
