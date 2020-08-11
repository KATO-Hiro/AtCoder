# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    next_cds = [int(input()) for _ in range(m)]
    cases = [i for i in range(1, n + 1)]
    cur_cd = 0

    for next_cd in next_cds:
        for index, case in enumerate(cases):
            if next_cd == case:
                cases[index] = cur_cd
                cur_cd = next_cd

    for case in cases:
        print(case)


if __name__ == '__main__':
    main()
