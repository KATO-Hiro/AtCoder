# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n % 2 == 1:
        print("error")
        exit()

    value_min = a[0]
    value_max = a[-1]
    ans = value_max - value_min

    if n >= 4:
        mod_a = a[1:-1]
        ans -= sum(mod_a[1::2])
        ans += sum(mod_a[::2])

    print(ans)


if __name__ == '__main__':
    main()
