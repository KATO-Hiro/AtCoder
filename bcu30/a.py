# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cur_pos = 0

    for ai in a:
        cur_pos += ai

        if cur_pos == n:
            print(cur_pos)
            exit()
        elif cur_pos > n:
            diff = cur_pos - n
            cur_pos = n - diff

    print(cur_pos)


if __name__ == '__main__':
    main()
