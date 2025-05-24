# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    x = int(input())

    while True:
        y = 0

        for si in s:
            if si.islower():
                if y + 1 == x:
                    print(si)
                    exit()

                y += 1
            else:
                count = int(si)

                if (count + 1) * y >= x:
                    x = x % y or y
                    break

                y += count * y


if __name__ == "__main__":
    main()
