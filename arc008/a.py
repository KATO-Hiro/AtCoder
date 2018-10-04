# -*- coding: utf-8 -*-


def main():
    n = int(input())

    # See:
    # https://beta.atcoder.jp/contests/arc008/submissions/1556856
    ans = n // 10 * 100
    ans += min(100, n % 10 * 15)
    print(ans)


if __name__ == '__main__':
    main()
