# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, t = map(int, input().split())
    e = [0]
    ans = n

    for i in range(m):
        ai, bi = map(int, input().split())
        e.append(ai)
        e.append(bi)

    e.append(t)

    for index, (ai, bi) in enumerate(zip(e, e[1:])):
        if index % 2 == 0:
            ans -= bi - ai
        else:
            ans += bi - ai
            ans = min(ans, n)

        if ans <= 0:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
