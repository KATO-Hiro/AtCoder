# -*- coding: utf-8 -*-


def main():
    s = input()[::-1]
    w_count = 0
    ans = 0

    for si in s:
        if si == 'W':
            w_count += 1
        else:
            ans += w_count

    print(ans)


if __name__ == '__main__':
    main()
