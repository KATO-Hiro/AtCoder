# -*- coding: utf-8 -*-


def main():
    s = input()
    k = int(input())
    one_count = 0

    for si in s:
        if si == '1':
            one_count += 1
        else:
            break

    if s[0] == '1':
        if k == 1:
            print(s[0])
        elif one_count >= k:
            print(1)
        elif one_count < k:
            print(s[one_count])
        else:
            print(s[1])
    else:
        print(s[0])


if __name__ == '__main__':
    main()
