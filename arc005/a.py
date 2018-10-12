# -*- coding: utf-8 -*-


def main():
    n = int(input())
    w = list(map(str, input().split()))
    count = 0

    # See:
    # https://beta.atcoder.jp/contests/arc005/submissions/1555860
    for wi in w:
        if '.' in wi:
            wi = wi.replace('.', '')

        if wi in ('TAKAHASHIKUN', 'Takahashikun', 'takahashikun'):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
