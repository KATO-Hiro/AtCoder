# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    si_size = len(s)
    ans = 0

    for _ in range(n):
        ti = input().rstrip()
        ti_size = len(ti)
        ok = False

        for begin in range(ti_size):
            for delta in range(1, ti_size):
                if s in "".join(ti[begin::delta]):
                    ok = True
                    break

        if ok:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
