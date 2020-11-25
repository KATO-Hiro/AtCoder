# -*- coding: utf-8 -*-


def main():
    n, x = map(int, input().split())
    s = input()

    for si in s:
        if si == "o":
            x += 1
        else:
            if x == 0:
                continue

            x -= 1

    print(x)


if __name__ == "__main__":
    main()
