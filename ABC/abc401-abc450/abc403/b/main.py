# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = input().rstrip()
    u = input().rstrip()
    n, m = len(t), len(u)

    for i in range(n - m + 1):
        s = t[i : i + m]
        ok = True

        for si, ui in zip(s, u):
            if si != "?" and si != ui:
                ok = False
                break

        if ok:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
