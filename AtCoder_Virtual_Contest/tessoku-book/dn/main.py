# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    ans = list()

    while x > 1 or y > 1:
        ans.append((x, y))

        if x >= y:
            x -= y
        else:
            y -= x

    # 復元
    print(len(ans))

    for xi, yi in ans[::-1]:
        print(xi, yi)


if __name__ == "__main__":
    main()
