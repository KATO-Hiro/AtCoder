# -*- coding: utf-8 -*-


def get_offset(alphabet: str, base_alphabet: str = "A") -> int:
    """Get offset between the base_alphabet and alphabet.

    Args:
        alphabet: The alphabet to use.
        base_alphabet: The base alphabet to use.

    Returns:
        difference between the base_alphabet and alphabet.

    See:
    https://docs.python.org/3.11/library/functions.html?highlight=chr#ord
    """

    return ord(alphabet) - ord(base_alphabet)


def main():
    import sys

    input = sys.stdin.readline

    p, q = input().rstrip().split()
    pi = get_offset(p)
    qi = get_offset(q)
    numbers = [3, 1, 4, 1, 5, 9]

    if pi > qi:
        pi, qi = qi, pi

    print(sum(numbers[pi:qi]))


if __name__ == "__main__":
    main()
