# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    adult_count = 0
    b = [0] * n

    for i in range(n):
        # 人iが成人になって、石を受け取る
        a[i] += adult_count
        adult_count += 1

        # 人iが新成人に石を配る
        # 配れる個数
        count = min(a[i], n - i - 1)
        # 人iがどの人まで配れるかをメモ
        b[i + count] += 1
        a[i] -= count

        # 成人のうち石を持っていない人数だけ減らす
        adult_count -= b[i]

    print(*a)


if __name__ == "__main__":
    main()
