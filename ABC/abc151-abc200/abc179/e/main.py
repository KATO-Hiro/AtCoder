# -*- coding: utf-8 -*-


def main():
    n, x, m = map(int, input().split())
    ans = x
    a = x
    d = dict()

    for i in range(2 * m + 1):
        a = (a ** 2) % m

        if a not in d.keys():
            d[a] = [i + 1]
        else:
            d[a].append(i + 1)

    for key, value in d.items():
        if len(value) == 1:
            count = 1
        else:
            d = value[1] - value[0]
            count = ((n - 1) - value[0]) // d + 1

        ans += key * count

    print(ans)


if __name__ == "__main__":
    main()
