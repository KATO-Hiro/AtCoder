# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    import sys

    input = sys.stdin.readline

    n, large_c = map(int, input().split())
    n_max = (2 * 10 ** 5) + 10
    stc = list()
    candidates = [0 for _ in range(n_max)]

    for i in range(n):
        si, ti, ci = map(int, input().split())
        stc.append((si, ti, ci))

    for cj in range(1, large_c + 1):
        time_table = [0 for _ in range(n_max)]

        for si, ti, ci in stc:
            if ci != cj:
                continue

            time_table[2 * si - 1] += 1
            time_table[2 * ti] -= 1

        time_table = list(accumulate(time_table))

        for index, t in enumerate(time_table):
            if t > 0:
                candidates[index] += 1

    print(max(candidates))


if __name__ == "__main__":
    main()
