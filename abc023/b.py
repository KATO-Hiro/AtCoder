# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    current_s = 'b'
    count = 0

    for i in range(1, n + 1):
        if current_s == s:
            print(count)
            exit()

        if i % 3 == 0:
            current_s = 'b' + current_s + 'b'
        elif i % 3 == 1:
            current_s = 'a' + current_s + 'c'
        elif i % 3 == 2:
            current_s = 'c' + current_s + 'a'

        count += 1

    print(-1)


if __name__ == '__main__':
    main()
