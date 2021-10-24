# -*- coding: utf-8 -*-


def main():
    s = input()

    if s[-2:] == "er":
        print("er")
    elif len(s) >= 3 and s[-3:] == "ist":
        print("ist")


if __name__ == "__main__":
    main()
