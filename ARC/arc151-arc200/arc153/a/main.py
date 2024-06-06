# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    numbers = list()

    for n12 in range(1, 10):
        for n3 in range(10):
            for n4 in range(10):
                for n56 in range(10):
                    for n79 in range(10):
                        for n8 in range(10):
                            number = (
                                [str(n12)] * 2
                                + [str(n3)]
                                + [str(n4)]
                                + [str(n56)] * 2
                                + [str(n79)]
                                + [str(n8)]
                                + [str(n79)]
                            )
                            numbers.append(int("".join(number)))

    print(numbers[n - 1])


if __name__ == "__main__":
    main()
