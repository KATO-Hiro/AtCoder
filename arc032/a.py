# -*- coding: utf-8 -*-


def main():
    n = int(input())
    sum_n = n * (n + 1) // 2

    if sum_n == 1:
        print('BOWWOW')
    else:
        x = [2]

        for i in range(2, n + 1):
            if all(i % j != 0 for j in x):
                x.append(i)

        for xi in x:
            if sum_n % xi == 0:
                print('BOWWOW')
                exit()

        print('WANWAN')


if __name__ == '__main__':
    main()
