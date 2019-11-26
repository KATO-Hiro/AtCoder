# -*- coding: utf-8 -*-


def main():
    from string import ascii_uppercase

    n = int(input())
    s = input()
    alpha = ascii_uppercase
    ans = ''

    for si in s:
        for index, a in enumerate(alpha):
            if si == a:
                next_index = (index + n) % 26
                ans += alpha[next_index]

    print(ans)


if __name__ == '__main__':
    main()
