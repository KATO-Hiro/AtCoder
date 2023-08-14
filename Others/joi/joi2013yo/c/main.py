# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    si_size = len(s)
    t = list()
    ans = 0

    for _ in range(n):
        ti = input().rstrip()
        ti_size = len(ti)
        ok = False

        for begin in range(ti_size):
            for delta in range(1, ti_size):
                u = ""

                for i in range(begin, ti_size, delta):
                    u += ti[i]

                    if len(u) == si_size and u == s:
                        ok = True
                        break

        if ok:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
