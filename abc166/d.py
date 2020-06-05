# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    x = int(input())

    # KeyInsight:
    # 範囲を絞り込んで、全探索
    for a in range(-200, 200):
        for b in range(-200, 200):
            if (a ** 5) - (b ** 5) == x:
                print(a, b)
                exit()

    print(-1)


if __name__ == '__main__':
    main()
