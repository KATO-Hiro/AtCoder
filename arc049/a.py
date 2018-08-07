# -*- coding: utf-8 -*-


def main():
    s = input()
    a, b, c, d = list(map(int, input().split()))
    result = ''

    s1 = s[:a]
    s2 = s[a:b]
    s3 = s[b:c]
    s4 = s[c:d]
    s5 = s[d:]

    if a == 0:
        s1 = '"' + s1
    else:
        s1 += '"'

    result = s1 + s2 + '"' + s3 + '"' + s4 + '"' + s5

    print(result)


if __name__ == '__main__':
    main()
