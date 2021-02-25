# -*- coding: utf-8 -*-


def main():
    s = input()

    for index, si in enumerate(s, 1):
        if index % 2 == 1:
            if si != si.lower():
                print("No")
                exit()
        else:
            if si != si.upper():
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
