# -*- coding: utf-8 -*-


def main():
    s = input()

    one = ["A", "D", "O", "P", "Q", "R"]
    two = ["B"]

    utpc = "0010"
    given = ""

    for si in s:
        if si in two:
            given += "2"
        elif si in one:
            given += "1"
        else:
            given += "0"

    if given == utpc:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
