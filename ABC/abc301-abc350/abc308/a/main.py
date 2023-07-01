# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(map(int, input().split()))
    t = sorted(s)

    if s != t:
        print("No")
        exit()

    for si in s:
        if 100 <= si <= 675 and si % 25 == 0:
            continue
        else:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
