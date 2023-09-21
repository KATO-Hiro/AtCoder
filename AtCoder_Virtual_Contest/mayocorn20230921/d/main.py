# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    n, h = map(int, input().split())
    katanas = list()

    for _ in range(n):
        ai, bi = map(int, input().split())
        katanas.append((ai, True))
        katanas.append((bi, False))

    katanas = sorted(katanas, key=lambda x: (x[0], -x[1]), reverse=True)
    ans = 0
    remain = h

    for ci, is_inf in katanas:
        if is_inf:
            ans += ceil(remain / ci)
            remain = 0
        else:
            ans += 1
            remain -= ci

        if remain <= 0:
            break

    print(ans)


if __name__ == "__main__":
    main()
