# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list(input().rstrip())
    t = s.count("T")
    a = n - t

    for i in range(m):
        ri = int(input())
        ri -= 1

        if s[ri] == "T":
            t -= 1
            a += 1
            s[ri] = "S"
        else:
            t += 1
            a -= 1
            s[ri] = "T"

        if t == 0 or a == 0:
            print(i + 1)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
