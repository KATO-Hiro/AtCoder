# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    m = 0
    plus = list()
    minus = list()

    for i, (si, ti) in enumerate(zip(s, t)):
        if si == ti:
            continue

        m += 1

        diff = ord(ti) - ord(si)

        if diff > 0:
            plus.append(i)
        elif diff < 0:
            minus.append(i)

    plus = plus[::-1]
    prev = list(s)

    print(m)

    for j in minus + plus:
        prev[j] = t[j]
        print("".join(prev))


if __name__ == "__main__":
    main()
