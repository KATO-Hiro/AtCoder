# -*- coding: utf-8 -*-


def main():
    n = int(input())
    plus = 0
    mul = 1

    for i in range(n):
        ci, ai = input().split()

        if ci == '+':
            plus += int(ai)
        elif ci == '*' and int(ai) > 0:
            mul *= int(ai)

    print(plus * mul)


if __name__ == '__main__':
    main()
