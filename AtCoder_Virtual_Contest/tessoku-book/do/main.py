# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]

    # 絶対値の記号を外す = + / -で4通り考える
    # op1 * ai + op2 * bi > 0のときだけ加算
    def f(op1, op2):
        summed = 0

        for ai, bi in ab:
            tmp = op1 * ai + op2 * bi

            if tmp > 0:
                summed += tmp

        return summed

    ans = f(1, 1)
    ans = max(ans, f(1, -1))
    ans = max(ans, f(-1, 1))
    ans = max(ans, f(-1, -1))

    print(ans)


if __name__ == "__main__":
    main()
