# -*- coding: utf-8 -*-


def main():
    a, b, c = list(map(int, input().split()))

    number_max = max(a, b, c)
    number_min = min(a, b, c)

    if a != number_max and a != number_min:
        print("A")
    elif b != number_max and b != number_min:
        print("B")
    else:
        print("C")


if __name__ == "__main__":
    main()
