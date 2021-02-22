# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())

    for _ in range(k):
        tmp = int("".join(sorted(str(n), reverse=True))) - int("".join(sorted(str(n))))
        n = tmp

    print(n)


if __name__ == "__main__":
    main()
