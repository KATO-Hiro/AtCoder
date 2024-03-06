# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a_max = 2 * 10**5 + 10
    count = [0] * a_max
    ans = 0

    # √a = dと変形
    # ルートの内部に残った整数が同じものを数える
    for ai in a:
        i = 2
        bi = ai

        while i**2 <= bi:
            while bi % (i**2) == 0:
                bi //= i**2

            i += 1

        ans += count[bi]
        count[bi] += 1

    # ai = 0の場合への対処
    ans += count[0] * (n - count[0])

    print(ans)


if __name__ == "__main__":
    main()
