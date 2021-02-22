# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())

    for _ in range(k):
        small = "".join(sorted(str(n)))
        large = small[::-1]
        n = int(large) - int(small)

    print(n)


if __name__ == "__main__":
    main()
