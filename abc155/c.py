# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    s = [input() for _ in range(n)]
    c = Counter(s)
    max_value = max(c.values())
    ans = list()

    for key, value in c.items():
        if value == max_value:
            ans.append(key)

    for a in sorted(ans):
        print(a)


if __name__ == '__main__':
    main()
