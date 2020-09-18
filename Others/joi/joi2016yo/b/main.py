# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]

    for k in range(1, m + 1):
        for index, (ai, aj) in enumerate(zip(a, a[1:])):
            if ai % k > aj % k:
                a[index] = aj
                a[index + 1] = ai

    print('\n'.join(map(str, a)))


if __name__ == '__main__':
    main()
