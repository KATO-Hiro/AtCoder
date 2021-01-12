# -*- coding: utf-8 -*-


def main():
    x = input()
    ans = 0

    for xi in x:
        ans = max(ans, int(xi))

    print(ans)


if __name__ == "__main__":
    main()
