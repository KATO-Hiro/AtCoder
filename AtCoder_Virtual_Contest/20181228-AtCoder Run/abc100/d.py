# -*- coding: utf-8 -*-


def main():
    from itertools import product

    n, m = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for op1, op2, op3 in list(product([1, -1], repeat=3)):
        tmp = [[0, 0, 0]] * n

        for index, value in enumerate(xyz):
            tmp[index] = sum([op1 * value[0], op2 * value[1], op3 * value[2]])

        camdidates = sorted(tmp, reverse=True)
        ans = max(ans, sum(camdidates[:m]))

    print(ans)


if __name__ == '__main__':
    main()
