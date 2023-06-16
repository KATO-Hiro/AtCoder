# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    # 体力・気力の下限値を全探索
    upper = 100
    ans = 0

    def f(a_min, b_min):
        a_max, b_max = a_min + k, b_min + k
        count = 0

        for ai, bi in ab:
            if a_min <= ai <= a_max and b_min <= bi <= b_max:
                count += 1

        return count

    for a_min in range(upper + 1):
        for b_min in range(upper + 1):
            ans = max(ans, f(a_min, b_min))

    print(ans)


if __name__ == "__main__":
    main()
