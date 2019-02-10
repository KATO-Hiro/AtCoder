# -*- coding: utf-8 -*-


def main():
    k, a, b = map(int, input().split())

    if k + 1 < a:
        print(k + 1)
    else:
        if a + 2 >= b:
            print(k + 1)
        else:
            count = k + 1 - a
            ans = count % 2
            exchange_count = count // 2
            ans += exchange_count * b - (exchange_count - 1) * a
            print(ans)


if __name__ == '__main__':
    main()
