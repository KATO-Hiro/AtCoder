# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n, k = map(int, input().split())
    s = list(input())

    nums = list()
    now = 1
    count = 0

    # See:
    # https://www.youtube.com/watch?v=FRzpDCx17vw
    # 1と0が連続していくつ続いているかを数える
    # 一つの配列で管理
    for si in s:
        if si == str(now):
            count += 1
        else:
            nums.append(count)
            now = 1 - now  # 0と1を切り替える
            count = 1

    # 端部の処理
    if count != 0:
        nums.append(count)

    # 1-0-1-0-1の形になっている必要がある
    if len(nums) % 2 == 0:
        nums.append(0)

    add = 2 * k + 1

    # 累積和
    summed = list(accumulate([0] + nums))

    tmp = 0
    ans = 0

    # 偶数番目に着目
    for i in range(0, len(nums), 2):
        left = i
        right = min(i + add, len(nums))
        tmp = summed[right] - summed[left]

        ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()
