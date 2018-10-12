# -*- coding: utf-8 -*-


def main():
    n = int(input())
    w = list(map(str, input().split()))
    count = 0

    for wi in w:
        if '.' in wi:
            wi = wi.replace('.', '')

        if wi == 'TAKAHASHIKUN':
            count += 1
        elif wi == 'Takahashikun':
            count += 1
        elif wi == 'takahashikun':
            count += 1

    print(count)


if __name__ == '__main__':
    main()
