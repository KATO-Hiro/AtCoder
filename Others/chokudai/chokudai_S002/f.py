# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = set()

    for i in range(n):
        ai, bi = map(int, input().split())

        if ai > bi:
            ans.add((bi, ai))
        else:
            ans.add((ai, bi))

    print(len(ans))


if __name__ == '__main__':
    main()
