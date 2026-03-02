# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()
    c = Counter(s)
    count_max = max(c.values())
    banned = set([key for key, value in c.items() if value == count_max])
    ans = []

    for si in s:
        if si in banned:
            continue

        ans.append(si)

    print("".join(ans))


if __name__ == "__main__":
    main()
