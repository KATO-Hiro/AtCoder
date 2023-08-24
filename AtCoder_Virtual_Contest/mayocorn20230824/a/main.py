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
    t = input().rstrip()
    count = set()

    for si, ti in zip(s, t):
        i = get_offset(si, "a")
        j = get_offset(ti, "a")
        count.add((j - i + 26) % 26)

    # print(count)

    if len(count) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
