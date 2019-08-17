# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    pre = s[0]
    ans = n
    i = 1

    while i < n:
        cur = s[i]

        if pre == cur:
            if i + 1 < n:
                pre = cur + s[i + 1]
                ans -= 1
        else:
            pre = cur

        i += 1

    print(ans)


if __name__ == '__main__':
    main()
