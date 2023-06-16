# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    ans = list()

    while x > 1 or y > 1:
        if x >= y:
            ans.append(0)
            x -= y
        else:
            ans.append(1)
            y -= x

    x, y = 1, 1

    # 復元
    print(len(ans))

    for flag in ans[::-1]:
        if flag:
            y += x
        else:
            x += y

        print(x, y)


if __name__ == "__main__":
    main()
