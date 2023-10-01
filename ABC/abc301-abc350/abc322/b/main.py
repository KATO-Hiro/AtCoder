# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = input().rstrip()
    t = input().rstrip()
    flag1 = t.startswith(s)
    flag2 = t.endswith(s)

    if flag1 and flag2:
        print(0)
    elif flag1 and not flag2:
        print(1)
    elif not flag1 and flag2:
        print(2)
    else:
        print(3)


if __name__ == "__main__":
    main()
