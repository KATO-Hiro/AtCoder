# -*- coding: utf-8 -*-


def main():
    from itertools import permutations

    s = list(input())
    n = len(s)
    count = [0 for _ in range(10)]
    numbers = list()

    if n == 1:
        if int(s[0]) % 8 == 0:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    elif n == 2:
        if (int(s[0] + s[1]) % 8 == 0) or (int(s[1] + s[0]) % 8 == 0):
            print("Yes")
            exit()
        else:
            print("No")
            exit()

    for si in s:
        number = int(si)
        count[number] += 1

        if count[number] <= 3:
            numbers.append(str(number))

    for first, second, third in list(permutations(numbers, 3)):
        digit_3 = first + second + third

        if int(digit_3) % 2 == 1:
            continue

        p, q = divmod(int(digit_3), 2)

        if (q == 0) and (p % 100) % 4 == 0:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
