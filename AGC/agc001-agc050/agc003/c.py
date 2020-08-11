# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    before = list()
    after = list()

    # 操作1を行う必要があるのは，
    # 操作をする前と条件を満たすよう操作した後で
    # 各要素の位置の偶奇が不一致のときではないか?
    for index, ai in enumerate(a, 1):
        before.append((ai, index % 2))

    for index, ai in enumerate(sorted(a), 1):
        after.append((ai, index % 2))

    count = 0

    for b, a in zip(sorted(before), after):
        if b[1] != a[1]:
            count += 1

    # 1回の操作で，2個の位置を変えられる
    print(count // 2)


if __name__ == '__main__':
    main()
