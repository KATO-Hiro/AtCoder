# -*- coding: utf-8 -*-


def count_niko_niko(n):
    return n * (n + 1) // 2


def main():
    s = input()
    n = len(s)
    count = 0
    ans = 0
    i = 0

    while i + 1 < n:
        if s[i] == '2' and s[i + 1] == '5':
            count += 1
            i += 2
        else:
            ans += count_niko_niko(count)
            count = 0
            i += 1

    if count > 0:
        ans += count_niko_niko(count)

    print(ans)


if __name__ == '__main__':
    main()
