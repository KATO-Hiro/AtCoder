# -*- coding: utf-8 -*-


def main():
    from math import ceil

    n = int(input())
    c = [int(input()) for _ in range(n)]
    colors = [1]
    ans = 1

    if len(set(c)) == 1:
        print(-1)
        exit()

    for index, ci in enumerate(c[1:], 1):
        if ci == c[index - 1]:
            colors[-1] += 1
        else:
            colors.append(1)

    for color in colors:
        ans = max(ans, ceil(color / 2))

    if c[0] == c[-1]:
        ans = max(ans, ceil((colors[0] + colors[-1]) / 2))

    print(ans)


if __name__ == '__main__':
    main()
