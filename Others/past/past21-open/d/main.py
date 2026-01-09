# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()
    c = Counter(s)
    ans = list()

    for si in s:
        if c[si] == 1:
            ans.append(si)

    print("".join(ans))


if __name__ == "__main__":
    main()
