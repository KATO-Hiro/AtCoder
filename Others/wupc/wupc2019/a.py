# -*- coding: utf-8 -*-


def main():
    s = input()[::-1]
    n = len(s)
    ans = ['' for _ in range(n)]

    if n == 1:
        print(s)
        exit()
    else:
        ans[0] = s[0]
        ans[1] = s[1]

        for i in range(n - 1):
            if ans[i] == 'A' and s[i + 1] == 'W':
                ans[i] = 'C'
                ans[i + 1] = 'A'
            else:
                ans[i + 1] = s[i + 1]

        print(''.join(map(str, ans))[::-1])


if __name__ == '__main__':
    main()
