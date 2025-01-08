# -*- coding: utf-8 -*-


def main():
    import sys
    from math import lcm

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, ai, mi = map(int, input().split())

        # 周期性を活用
        lcm_i = lcm(ai, mi)
        l = list()
        s = set()
        summed = 0

        for mod in range(ai, lcm_i + 1, ai):
            while summed < mod:
                summed += mi

            result = summed - mod

            if result in s:
                break

            l.append(result)
            s.add(result)

        size = len(l)
        p, q = divmod(n, size)
        total = sum(l) * p + sum(l[:q])
        print(total)


if __name__ == "__main__":
    main()
