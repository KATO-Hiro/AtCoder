# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 1

    if 0 in a:
        print(0)
        exit()

    for ai in a:
        ans *= ai

        if ans > 10 ** 18:
            print(-1)
            exit()

    print(ans)


if __name__ == '__main__':
    main()
