# -*- coding: utf-8 -*-


def main():
    s = input()

    if (
        (s[0] == s[1] == s[2] == "o")
        or (s[1] == s[2] == s[3] == "o")
        or (s[2] == s[3] == s[4] == "o")
    ):
        print("o")
    elif (
        (s[0] == s[1] == s[2] == "x")
        or (s[1] == s[2] == s[3] == "x")
        or (s[2] == s[3] == s[4] == "x")
    ):
        print("x")
    else:
        print("draw")


if __name__ == "__main__":
    main()
