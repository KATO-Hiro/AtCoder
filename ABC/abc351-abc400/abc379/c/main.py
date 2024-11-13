# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    y = [(xi, ai) for xi, ai in zip(x, a)]
    y = sorted(y) + [(n + 1, 1)]

    # 番兵を置く
    prev_xi, count = 0, 1
    ans = 0

    for xi, ai in y:
        l = xi - prev_xi
        carry = count - l

        ans += l * (l - 1) // 2
        ans += l * carry

        if carry < 0:
            ans = -1
            break

        prev_xi = xi
        count = carry + ai

    if count != 1:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
