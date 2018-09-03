# -*- coding: utf-8 -*-


def main():
    n = int(input())
    x = list()
    ans = 0

    for i in range(n):
        xi = input()
        ans += xi.count('x')
        x.append(list(xi))

    for col in range(9):
        pre = x[0][col]

        if pre == 'o':
            ans += 1

        for row in range(1, n):
            cur = x[row][col]

            if pre != 'o' and cur == 'o':
                ans += 1

            pre = cur

    print(ans)


if __name__ == '__main__':
    main()
