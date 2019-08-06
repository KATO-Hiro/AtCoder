# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    cur_s = 'b'

    for i in range(1, 101):
        if len(cur_s) >= len(s):
            if cur_s == s:
                print(0)
                exit()
            else:
                print(-1)
                exit()

        if i % 3 == 0:
            cur_s = 'b' + cur_s + 'b'
        elif i % 3 == 1:
            cur_s = 'a' + cur_s + 'c'
        elif i % 3 == 2:
            cur_s = 'c' + cur_s + 'a'

        if cur_s == s:
            print(i)
            exit()


if __name__ == '__main__':
    main()
