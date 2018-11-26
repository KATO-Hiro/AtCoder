# -*- coding: utf-8 -*-
ans = [100, 100, 200] + [0] * 17


def f(i):
    if i == 20:
        return ans[19]

    ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]

    return f(i + 1)


def main():
    print(f(3))


if __name__ == '__main__':
    main()
