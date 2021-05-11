# -*- coding: utf-8 -*-


def main():
    s = input()
    ans = 0

    for i in range(9):
        if s[i : i + 4] == "ZONe":
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
