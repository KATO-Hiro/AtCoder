# -*- coding: utf-8 -*-


def main():
    s = input()

    # See:
    # https://atcoder.jp/contests/abc175/submissions/15907467
    # Pythonのシンタックスを活用
    if 'RRR' in s:
        print(3)
    elif 'RR' in s:
        print(2)
    elif 'R' in s:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
