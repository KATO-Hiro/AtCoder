# -*- coding: utf-8 -*-


def main():
    s = input()
    ans = ''

    for si in s:
        if si == 'O':
            ans += 'A'
        elif si == 'A':
            ans += 'O'
        else:
            ans += si

    print(ans)


if __name__ == '__main__':
    main()
