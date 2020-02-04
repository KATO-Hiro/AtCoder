# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = float('inf')

    # KeyInsigh: bit全探索
    # 1つだけWAが取れなかった
    # See:
    # https://atcoder.jp/contests/s8pc-4/submissions/2122030
    if n == 1:
        print(0)
        exit()

    for bit in range(1 << (n - 1)):
        color_count = 1
        cost = 0
        height_min = a[0]

        for j in range(n - 1):
            # 高さを変更しなくても、条件を満たしている
            if height_min < a[j + 1]:
                color_count += 1
                height_min = a[j + 1]
                continue

            if bit & (1 << j):
                cost += height_min - a[j + 1] + 1
                color_count += 1
                height_min += 1

        if color_count >= k:
            ans = min(ans, cost)

    print(ans)


if __name__ == '__main__':
    main()
