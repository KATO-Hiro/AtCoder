# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    s = input()
    pos = list()
    prev = s[0]

    if prev == '0':
        pos.append(1)

    for i in range(1, n):
        if s[i] == '0' and (s[i - 1] != '0'):
            pos.append(i + 1)
        elif (i == n - 1) and (s[i] == '1'):
            pos.append(i + 1)

    m = len(pos)

    if (m - k + 1) <= 0:
        print(n)
    else:
        from bisect import bisect_left

        one = [0 for _ in range(n + 1)]
        zero = [0 for _ in range(n + 1)]

        for index, si in enumerate(s):
            if si == '0':
                zero[index + 1] = zero[index] + 1
                one[index + 1] = one[index]
            elif si == '1':
                zero[index + 1] = zero[index]
                one[index + 1] = one[index] + 1

        print(one, zero)
        print(pos)

        for j in range(m - k + 1):
            print(j)


if __name__ == '__main__':
    main()
