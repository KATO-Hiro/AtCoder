# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    one, ten, hundred = 0, 0, 0

    for ai in a:
        ai %= 1000
        remain = 0

        if ai != 0:
            remain = 1000 - ai

        i = 0

        while remain > 0:
            remain, q = divmod(remain, 10)

            if i == 0:
                one += q
            elif i == 1:
                ten += q
            else:
                hundred += q

            i += 1

    print(one, ten, hundred)


if __name__ == "__main__":
    main()
