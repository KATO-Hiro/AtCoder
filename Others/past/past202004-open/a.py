# -*- coding: utf-8 -*-


def main():
    s, t = input().split()

    if 'B' in s and 'B' in t:
        print(abs(int(s[1]) - int(t[1])))
    elif 'F' in s and 'F' in t:
        print(abs(int(s[0]) - int(t[0])))
    elif 'B' in s and 'F' in t:
        print((int(s[1]) + int(t[0])) - 1)
    elif 'F' in s and 'B' in t:
        print((int(s[0]) + int(t[1])) - 1)


if __name__ == '__main__':
    main()
