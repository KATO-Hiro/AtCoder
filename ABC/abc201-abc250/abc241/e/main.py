# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = 0
    memo_i, memo_x = defaultdict(int), defaultdict(int)

    # See:
    # https://www.youtube.com/watch?v=sN2AqHqLzdg
    for i in range(k):
        mod_n = x % n

        # ループを検出
        if mod_n in memo_i.keys():
            period = i - memo_i[mod_n]

            # ちょうどのとき
            if (k - i) % period == 0:
                x += (k - i) // period * (x - memo_x[mod_n])
                break

        memo_i[mod_n] = i
        memo_x[mod_n] = x
        x += a[mod_n]

    print(x)


if __name__ == "__main__":
    main()
