# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    dis_liked_numbers = [2, 4, 5, 6, 8]
    ans = 0

    for ai in a:
        while True:
            if ai in dis_liked_numbers:
                ai -= 1
                ans += 1
            else:
                break

    print(ans)


if __name__ == '__main__':
    main()
