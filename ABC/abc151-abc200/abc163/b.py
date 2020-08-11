# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    diff = n - sum(a)

    if diff < 0:
        print(-1)
    else:
        print(diff)


if __name__ == '__main__':
    main()
