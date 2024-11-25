# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    c = Counter()

    if n % 2 != 0:
        print("No")
        exit()

    for i in range(n // 2):
        i2 = i * 2
        j2 = i * 2 + 1

        if s[i2] != s[j2]:
            print("No")
            exit()

        if s[i2] in c:
            print("No")
            exit()

        c[s[i2]] += 1

    print("Yes")


if __name__ == "__main__":
    main()
