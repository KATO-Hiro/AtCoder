# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())
    ans = 0
    i = 1
    cur_count = 0

    while cur_count < c:
        cur_count += a

        if i % 7 == 0:
            cur_count += b

        i += 1
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
