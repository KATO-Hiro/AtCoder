# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = [None for _ in range(n)]

    for i in range(n):
        si = set(input())
        s[i] = si

    ans = ''

    for j in range(n // 2):
        common = s[j] & s[(n - 1) - j]

        if len(common) >= 1:
            ans += common.pop()
        else:
            print(-1)
            exit()

    if n % 2 == 0:
        print(ans + ans[::-1])
    else:
        print(ans + s[n // 2].pop() + ans[::-1])


if __name__ == '__main__':
    main()
