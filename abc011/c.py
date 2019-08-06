# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ngs = [int(input()) for _ in range(3)]
    numbers = [i for i in range(300 + 2) if i not in ngs]

    # Not solve.
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]

        if diff >= 4:
            print('NO')
            exit()
        else:
            if numbers[i + 1] == n:
                print('YES')
                exit()
            elif numbers[i + 1] > n:
                print('NO')
                exit()


if __name__ == '__main__':
    main()
