# -*- coding: utf-8 -*-


def main():
    from re import compile

    a, b = map(str, input().split())
    s = input()
    pattern = '[0-9]{' + a + '}-{1}[0-9]{' + b + '}'
    re_pattern = compile(pattern)
    result = re_pattern.match(s)

    if result:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
