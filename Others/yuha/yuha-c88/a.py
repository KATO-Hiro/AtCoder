# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = ''

    for i in range(n):
        p, q, r = input().split()

        if p == 'BEGINNING':
            ans += r[0]
        elif p == 'MIDDLE':
            ans += r[len(r) // 2]
        elif p == 'END':
            ans += r[-1]

    print(ans)


if __name__ == '__main__':
    main()
