# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    a, b, c = map(int, input().split())

    # See:
    # https://www.youtube.com/watch?v=bHzohtVsG0Q&feature=youtu.be
    # KeyInsight: 整数で比較する．両辺を意味を変えずに変形
    # ハマった点: 小数同士で比較しようとしていた

    # √a + √b < √c
    # (√a + √b) ** 2 < √c ** 2
    # a + 2√ab + b < c
    # 2√ab < c - (a + b)
    # 4ab < (c - (a + b)) ** 2
    diff = c - (a + b)

    # 右辺は、0以上でないといけない
    if diff < 0:
        print('No')
        exit()

    if (4 * a * b) < (diff ** 2):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
