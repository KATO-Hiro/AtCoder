# -*- coding: utf-8 -*-


def main():
    from string import ascii_lowercase
    import sys

    input = sys.stdin.readline
    alpha = ascii_lowercase

    s = input().rstrip()
    t = input().rstrip()
    c = set()

    for si, ti in zip(s, t):
        c.add((alpha.index(si) - alpha.index(ti)) % 26)

    if len(c) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
