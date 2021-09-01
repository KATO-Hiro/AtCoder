# -*- coding: utf-8 -*-


def main():
    x, y = list(map(int, input().split(".")))
    x = str(x)

    if y <= 2:
        print(x + "-")
    elif y <= 6:
        print(x)
    else:
        print(x + "+")


if __name__ == "__main__":
    main()
