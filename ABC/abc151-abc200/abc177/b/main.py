# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    t = input()
    m = len(t)
    ans = float('inf')

    for i in range(n - m + 1):
        u = s[i:i + m]

        count = 0

        for ui, ti in zip(u, t):
            if ui != ti:
                count += 1

        ans = min(ans, count)

    print(ans)


if __name__ == '__main__':
    main()
