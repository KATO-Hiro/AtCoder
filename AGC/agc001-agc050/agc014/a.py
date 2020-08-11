# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())
    ans = 0

    # See:
    # https://www.youtube.com/watch?v=UHfTqvaD0pk
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        print(0)
        exit()

    if b == c == a:
        print(-1)
        exit()

    for i in range(1, 31):
        twice = 2 ** i
        tmp = twice % 3

        x = twice // 3
        y = x
        z = x

        if tmp == 2:
            y += 1
            z += 1
        elif tmp == 1:
            x += 1

        takahashi = a * x + b * y + c * z
        aoki = a * y + b * x + c * z
        snuke = a * z + b * y + c * x

        if takahashi % twice == 0 and aoki % twice == 0 and snuke % twice == 0:
            ans += 1
        else:
            print(ans)
            exit()


if __name__ == '__main__':
    main()
