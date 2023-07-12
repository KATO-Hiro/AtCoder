# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 1 << 60

    for pattern in product([0, 1], repeat=n):
        inner, out = 0, 0

        for pi, ai in zip(pattern, a):
            inner |= ai

            # 区切り
            if pi == 1:
                out ^= inner
                inner = 0

        # 最後の区間が反映されていない場合
        if pattern[-1] == 0:
            out ^= inner

        ans = min(ans, out)

    print(ans)


if __name__ == "__main__":
    main()
