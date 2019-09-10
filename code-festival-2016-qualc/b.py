# -*- coding: utf-8 -*-


def main():
    k, t = map(int, input().split())
    a = list(map(int, input().split()))
    max_value = 0
    max_value_index = -1
    ans = 0

    for index, ai in enumerate(a):
        if ai > max_value:
            max_value = ai
            max_value_index = index

    prev = max_value_index
    a[prev] -= 1

    # KeyInsight
    # できる限り前と同じケーキを選ばないようにしながら，残りが最も多いケーキを選択
    # See:
    # http://competitive-kivantium.hateblo.jp/entry/2016/10/24/135521
    for i in range(k - 1):
        max_value = 0
        max_value_index = -1

        # 残りのケーキが最大となるものを求める
        for j in range(t):
            if a[j] > max_value and j != prev:
                max_value = a[j]
                max_value_index = j

        if max_value_index != -1:
            prev = max_value_index
            a[max_value_index] -= 1
        else:
            a[prev] -= 1
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
