# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    all = False
    used = set()
    value = 0

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            all = True
            used = set()
            value = qi[1]
        elif qi[0] == 2:
            iq, xq = qi[1:]
            iq -= 1

            if all:
                if iq in used:
                    a[iq] += xq
                else:
                    a[iq] = value + xq
                    used.add(iq)
            else:
                a[iq] += xq
        else:
            iq = qi[1] - 1

            if all:
                if iq in used:
                    print(a[iq])
                else:
                    print(value)
                pass
            else:
                print(a[iq])


if __name__ == "__main__":
    main()
