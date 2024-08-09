# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    d = {
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
    }

    ans = ""

    for _ in range(n):
        si = input().rstrip()
        ans += d[si]

    print(ans)


if __name__ == "__main__":
    main()
