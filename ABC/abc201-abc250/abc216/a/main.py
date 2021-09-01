# -*- coding: utf-8 -*-


def main():
    xy = input().split(".")

    if 0 <= int(xy[1]) <= 2:
        print(xy[0] + "-")
    elif 3 <= int(xy[1]) <= 6:
        print(xy[0])
    else:
        print(xy[0] + "+")


if __name__ == "__main__":
    main()
