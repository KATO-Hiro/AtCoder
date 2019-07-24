# -*- coding: utf-8 -*-


def main():
    n, q = map(int, input().split())
    ans = "kogakubu10gokan"

    for i in range(n):
        year, name = input().split()

        if int(year) <= q:
            ans = name

    print(ans)


if __name__ == '__main__':
    main()
