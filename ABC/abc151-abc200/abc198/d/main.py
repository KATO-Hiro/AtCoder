# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    s1 = list(input().rstrip())
    s2 = list(input().rstrip())
    s3 = list(input().rstrip())
    s = set(s1) | set(s2) | set(s3)

    if len(s) > 10:
        print("UNSOLVABLE")
        exit()

    n = len(s)

    for p in permutations(range(10), r=n):
        d = dict()

        for index, si in enumerate(s):
            d[si] = str(p[index])

        n1, n2, n3 = "", "", ""

        for s1i in s1:
            n1 += d[s1i]
        for s2i in s2:
            n2 += d[s2i]
        for s3i in s3:
            n3 += d[s3i]

        if n1[0] == "0" or n2[0] == "0" or n3[0] == "0":
            continue

        if int(n1) + int(n2) == int(n3):
            print("\n".join(map(str, [n1, n2, n3])))
            exit()

    print("UNSOLVABLE")


if __name__ == "__main__":
    main()
