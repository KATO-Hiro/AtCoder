# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    h_max = max(h)
    ans = 0

    for _ in range(h_max):
        # print(h)
        hi_min = h_max
        tmp = list()

        for i in range(n):
            hi = h[i]

            if hi == 0:
                for tmp_i in tmp:
                    h[tmp_i] -= hi_min

                if len(tmp) > 0:
                    ans += hi_min

                hi_min = h_max
                tmp = list()
            else:
                hi_min = min(hi_min, hi)
                tmp.append(i)

        if len(tmp) > 0:
            for tmp_i in tmp:
                h[tmp_i] -= hi_min

            ans += hi_min

        if sum(h) == 0:
            break

    print(ans)


if __name__ == "__main__":
    main()
