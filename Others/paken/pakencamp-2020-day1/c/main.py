# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = dict()

    for i in range(n):
        k = int(input())
        s = input().split()

        for si in s:
            si = si.rstrip()

            if si not in d.keys():
                d[si] = 1
            else:
                d[si] += 1

    ans = 0

    for key, value in d.items():
        if value == n:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
