# -*- coding: utf-8 -*-


def main():
    n = int(input())
    t = list(input())

    if n < 3:
        if n == 1 and t[0] == "0":
            print(10 ** 10)
            exit()
        elif n == 1 and t[0] == "1":
            print(2 * 10 ** 10)
            exit()
        elif n == 2 and t[0] == "1":
            print(10 ** 10)
            exit()

    count = 0
    left = 0
    right = n

    if t[0] == "0":
        left += 1
        count += 1
    elif t[0] == "1" and t[1] == "0":
        left += 2
        count += 1

    if t[-2] == "1" and t[-1] == "1":
        right -= 2
        count += 1
    elif t[-2] == "0" and t[-1] == "1":
        right -= 1
        count += 1

    diff = right - left

    if diff % 3 != 0:
        print(0)
        exit()

    for i in range(diff // 3):
        j = 3 * i + left

        if t[j] == "1" and t[j + 1] == "1" and t[j + 2] == "0":
            count += 1
        else:
            print(0)
            exit()

    print(10 ** 10 - count + 1)


if __name__ == "__main__":
    main()
