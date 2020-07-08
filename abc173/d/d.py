# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)

    # KeyInsight:
    # 順番が重要でない場合の数列は、ひとまずソートする
    # 最大値の証明は、「この値にできる」「これより良い値にできない」を示すのが定石
    ans = a[0]

    if n % 2 == 0:
        m = (n - 1) // 2
    else:
        m = (n - 2) // 2

    for i in range(m):
        ans += a[i + 1] * 2

    if n % 2 == 1:
        ans += a[m + 1]

    print(ans)


if __name__ == '__main__':
    main()
