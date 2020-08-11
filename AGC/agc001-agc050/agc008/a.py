# -*- coding: utf-8 -*-


def main():
    x, y = map(int, input().split())

    # KeyInsight
    # 最短の操作方法は，ボタンBを0回か1回押す，ボタンAを0回以上押す，ボタンBを0回か1回押す
    # 4通りを試す
    # y >= xが成り立てば，y - x回で目標を達成できる
    # 4通りの最小値が答え
    xy = [(x, y, 0), (x, -y, 1), (-x, y, 1), (-x, -y, 2)]
    ans = float('inf')

    for xi, yi, count in xy:
        if yi >= xi:
            ans = min(ans, yi - xi + count)

    print(ans)


if __name__ == '__main__':
    main()
