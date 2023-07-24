# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    c = list()

    cond1 = s[0] == "A"

    for i in range(2, n - 1):
        if s[i] == "C":
            c.append(i)

    cond2 = len(c) == 1
    ok = True

    for i, si in enumerate(s):
        if i == 0 or (len(c) >= 1 and i == c[0]):
            continue

        if si != si.lower():
            ok = False
            break

    if cond1 == cond2 == ok == True:
        print("AC")
    else:
        print("WA")


if __name__ == "__main__":
    main()
