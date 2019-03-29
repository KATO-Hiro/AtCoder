# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    ans = 0

    for i in range(1, n + 1):
        for j in range(n - i + 1):
            t = s[j:j + i]

            if len(t.replace('A', '').replace('C', '').replace('G', '').replace('T', '')) == 0:
                ans = max(ans, i)

    print(ans)


if __name__ == '__main__':
    main()
