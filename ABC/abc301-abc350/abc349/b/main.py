# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()
    c = Counter(s)
    d = Counter(c.values())
    flag = all([value == 2 for value in d.values()])

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
