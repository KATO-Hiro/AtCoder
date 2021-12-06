# -*- coding: utf-8 -*-


def main():
    n = int(input())

    if n >= 42:
        n += 1

    ans = "AGC0"

    if n < 10:
        ans += "0"
        ans += str(n)
    else:
        ans += str(n)

    print(ans)


if __name__ == "__main__":
    main()
