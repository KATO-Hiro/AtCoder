# -*- coding: utf-8 -*-


def main():
    n = int(input())
    odds = [i for i in range(1, 201) if i % 2 == 1]
    ans = 0

    for j in range(1, n + 1):
        count = 0

        for odd in odds:
            if j % odd == 0:
                count += 1

        if count == 8:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
