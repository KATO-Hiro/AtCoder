# -*- coding: utf-8 -*-


def main():
    s = list(map(int, input()))
    n = len(s)

    case1 = [0] * n
    case2 = [0] * n

    for i in range(n):
        if i % 2 == 0:
            case1[i] = 1
        else:
            case2[i] = 1

    count1 = 0
    count2 = 0

    for one, si in zip(case1, s):
        if one != si:
            count1 += 1

    for two, si in zip(case2, s):
        if two != si:
            count2 += 1

    print(min(count1, count2))


if __name__ == '__main__':
    main()
