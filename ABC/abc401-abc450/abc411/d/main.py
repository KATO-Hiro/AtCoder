# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    qs = list()

    for _ in range(q):
        qi = list(input().rstrip().split())
        query, p = int(qi[0]), int(qi[1])

        if query == 2:
            qs.append((query, p, qi[2][::-1]))
        else:
            qs.append((query, p))

    i = 0
    ans = list()

    for q in qs[::-1]:
        query, p = int(q[0]), int(q[1])

        if query == 1:
            if i == p:
                i = 0
        elif query == 2:
            if i == p:
                ans += list(q[2])
        else:
            if i == 0:
                i = p

    print("".join(ans[::-1]))


if __name__ == "__main__":
    main()
