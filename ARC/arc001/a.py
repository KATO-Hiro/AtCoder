# -*- coding: utf-8 -*-


def main():
    n = int(input())
    c = input()

    # See:
    # https://beta.atcoder.jp/contests/arc001/submissions/1613525
    count_strings = [c.count(str(i)) for i in range(1, 5)]
    print(max(count_strings), min(count_strings))


if __name__ == '__main__':
    main()
