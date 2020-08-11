# -*- coding: utf-8 -*-


def main():
    s = input()

    # See:
    # https://beta.atcoder.jp/contests/arc019/submissions/2489032
    # https://docs.python.jp/3/library/stdtypes.html#str.translate
    # https://docs.python.jp/3/library/stdtypes.html#str.maketrans
    print(s.translate(str.maketrans('ODIZSB', '001258')))


if __name__ == '__main__':
    main()
