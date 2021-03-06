# -*- coding: utf-8 -*-


def main():
    n = int(input())
    dishes = list()
    ans = 0

    # See:
    # https://poporix.hatenablog.com/entry/2019/01/28/222905
    # https://misteer.hatenablog.com/entry/NIKKEI2019qual?_ga=2.121425408.962332021.1548821392-1201012407.1527836447
    for i in range(n):
        ai, bi = map(int, input().split())
        dishes.append((ai, bi))

    for index, dish in enumerate(sorted(dishes, key=lambda x: x[0] + x[1], reverse=True)):
        if index % 2 == 0:
            ans += dish[0]
        else:
            ans -= dish[1]

    print(ans)


if __name__ == '__main__':
    main()
