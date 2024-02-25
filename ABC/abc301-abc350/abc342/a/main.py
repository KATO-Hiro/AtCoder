# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()
    c = Counter(s)

    for key, value in c.items():
        if value != 1:
            continue

        for i, si in enumerate(s, 1):
            if si == key:
                print(i)
                exit()


if __name__ == "__main__":
    main()
