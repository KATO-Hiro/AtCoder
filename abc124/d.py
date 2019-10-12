# -*- coding: utf-8 -*-


def main():
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

    # 1. left，rightをfor文の前に
    left = 0
    right = 0  # [left, right)
    tmp = 0
    ans = 0

    # 偶数番目に着目
    for i in range(0, len(nums), 2):
        # 2. 次のleft, rightを決める
        next_left = i
        next_right = min(i + add, len(nums))

        # 3.
        # 左端を移動
        while next_left > left:
            tmp -= nums[left]
            left += 1

        # 右端を移動
        while next_right > right:
            tmp += nums[right]
            right += 1

        ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()
