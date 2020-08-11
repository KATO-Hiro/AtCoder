# -*- coding: utf-8 -*-


def main():
    h, w, a, b = map(int, input().split())
    ans = [[0 for _ in range(w)] for _ in range(h)]

    # See:
    # https://www.youtube.com/watch?v=RXYksUjlPD4
    # KeyInsight
    # 以下の形式で埋める
    # －－－－－
    # |000|1111|
    # |000|1111|
    # －－－－－
    # |111|0000|
    # －－－－－
    # 思いつくためには，最初の行・列が条件を満たす場合を考える
    # 今回，Noのケースはない
    for wi in range(a, w):
        for hi in range(b):
            ans[hi][wi] = 1

    for hi in range(b, h):
        for wi in range(a):
            ans[hi][wi] = 1

    for a in ans:
        print(''.join(map(str, a)))


if __name__ == '__main__':
    main()
