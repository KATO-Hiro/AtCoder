# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    count = 0

    # See:
    # https://atcoder.jp/contests/hhkb2020/submissions/17289933
    for row in s:
        for first, second in zip(row, row[1:]):
            if first == second == ".":
                count += 1

    # zip(*hoge)で、縦横を入れ替えている
    for col in zip(*s):
        print(col)
        for first, second in zip(col, col[1:]):
            if first == second == ".":
                count += 1

    print(count)


if __name__ == "__main__":
    main()
