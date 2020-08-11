# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = ['a', 'b', 'c', 'd', 'e']

    for i in range(1, n + 1):
        ans = ''

        for index, k in enumerate([2, 3, 4, 5, 6]):
            if i % k == 0:
                ans += s[index]

        if ans == '':
            ans = str(i)

        print(ans)


if __name__ == '__main__':
    main()
