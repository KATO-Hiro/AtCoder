# -*- coding: utf-8 -*-


def my_round(val):
    if val % 10 == 0:
        return val
    else:
        return val + (10 - val % 10)


def main():
    alpha = [int(input()) for _ in range(5)]
    ans = [0 for _ in range(5)]

    for i in range(5):
        for j, a in enumerate(alpha):
            if i == j:
                ans[i] += a
            else:
                ans[i] += my_round(a)

    print(min(ans))


if __name__ == '__main__':
    main()
