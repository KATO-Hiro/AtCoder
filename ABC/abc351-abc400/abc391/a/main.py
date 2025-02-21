# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    dir = {
        "N": "S",
        "S": "N",
        "E": "W",
        "W": "E",
        "NE": "SW",
        "SW": "NE",
        "NW": "SE",
        "SE": "NW",
    }

    s = input().rstrip()
    t = dir[s]
    print(t)


if __name__ == "__main__":
    main()
