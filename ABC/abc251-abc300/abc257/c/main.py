# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    w = list(map(int, input().split()))
    y = list()

    # 全員大人と仮定
    count = s.count("1")
    ans = count

    # 体重で昇順ソート
    for si, wi in zip(s, w):
        y.append((wi, si))
    
    y = sorted(y)

    for i, (_, si) in enumerate(y):
        if si == "0":
            count += 1
        else:
            count -= 1

        if (i < n - 1) and y[i][0] == y[i + 1][0]:
            continue

        ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
