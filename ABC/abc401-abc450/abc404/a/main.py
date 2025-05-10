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


def add_offset_to_alphabet(offset: int, base_alphabet: str = "A") -> str:
    """Add offset to the base_alphabet.

    Args:
        offset: Difference from the base alphabet.
        base_alphabet: The base alphabet to use.

    Returns:
        Corrected alphabet.

    See:
    https://docs.python.org/3.11/library/functions.html?highlight=chr#ord
    """

    return chr(ord(base_alphabet) + offset)


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    used = [False] * 26

    for si in s:
        offset = get_offset(si, "a")
        used[offset] = True

    for i, u in enumerate(used):
        if u:
            continue

        ans = add_offset_to_alphabet(i, "a")
        print(ans)
        break


if __name__ == "__main__":
    main()
