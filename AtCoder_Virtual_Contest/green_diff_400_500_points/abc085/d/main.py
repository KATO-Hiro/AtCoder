# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    n, h = map(int, input().split())
    ab = list()

    for i in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, False))
        ab.append((bi, True))

    ab = sorted(ab, reverse=True)
    ans = 0

    for ab_i, is_throw in ab:
        if is_throw:
            h -= ab_i
            ans += 1

            if h <= 0:
                break
        else:
            ans += ceil(h / ab_i)
            break

    # print(ab)
    print(ans)


if __name__ == "__main__":
    main()
