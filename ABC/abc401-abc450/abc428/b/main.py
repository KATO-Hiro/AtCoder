# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()
    d = defaultdict(int)

    for i in range(n):
        if i + k > n:
            break

        t = s[i : i + k]
        d[t] += 1

    count_max = max(d.values())
    ans = list()

    for key, value in d.items():
        if value == count_max:
            ans.append(key)

    ans.sort()

    print(count_max)
    print(*ans)


if __name__ == "__main__":
    main()
