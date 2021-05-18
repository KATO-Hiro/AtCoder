# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    ans = 0

    for number in range(10 ** 4):
        n = str(number).zfill(4)

        for index, si in enumerate(s):
            if si == "o" and not (str(index) in n):
                break
            if si == "x" and (str(index) in n):
                break
        else:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
