# -*- coding: utf-8 -*-


def main():
    r, g, b, n = map(int, input().split())
    ans = 0

    for i in range(3000 + 1):
        for j in range(3000 + 1):
            diff = n - (r * i + g * j)

            if diff >= 0 and (diff % b == 0):
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
