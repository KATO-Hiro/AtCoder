# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = 0

    for si, ai in zip(s, a):
        ans = max(ans, si * ai)

    print(ans)


if __name__ == '__main__':
    main()
