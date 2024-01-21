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

    s = input().rstrip()
    t = list()

    for si in s:
        t.append(get_offset(si))

    for first, second in zip(t, t[1:]):
        if first > second:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
