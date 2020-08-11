# -*- coding: utf-8 -*-


def main():
    r, d, x2000 = map(int, input().split())
    pre = x2000

    for i in range(10):
        ans = r * pre - d
        print(ans)
        pre = ans


if __name__ == '__main__':
    main()
