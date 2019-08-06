# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n, k = map(int, input().split())
    a = list(accumulate([0] + list(map(int, input().split()))))
    bit_groups = list()

    for j in range(1, n + 1):
        for i in range(j, n + 1):
            bit = bin(a[i] - a[j - 1])[2:]
            length = len(bit)

            if length < 41:
                bit = '0' * (41 - length) + bit

            bit_groups.append(bit)

    ans = 0
    digit_max = 41

    for i in range(digit_max):
        count = 0

        for bit_group in bit_groups:
            if int(bit_group, 2) >= ans and bit_group[i] == '1':
                count += 1

        if count >= k:
            ans += 2 ** ((digit_max - 1) - i)

    print(ans)


if __name__ == '__main__':
    main()
