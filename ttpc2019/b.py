# -*- coding: utf-8 -*-


def main():
    import re

    n = int(input())
    pattern = ".*" + "okyo" + ".*" + "ech" + ".*"

    for i in range(n):
        s = input()

        compiled = re.compile(pattern)
        result = compiled.match(s)

        if result:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
