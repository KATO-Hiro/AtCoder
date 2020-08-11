# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = 0

    for i in range(n):
        xi, ui = input().split()

        if ui == 'JPY':
            ans += float(xi)
        else:
            ans += float(xi) * 380000

    print(ans)


if __name__ == '__main__':
    main()
