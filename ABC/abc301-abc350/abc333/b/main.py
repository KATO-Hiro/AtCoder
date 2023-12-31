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
    from collections import Counter

    input = sys.stdin.readline

    s = list(input().rstrip())
    t = list(input().rstrip())
    c = Counter()

    for si, tj in zip(s, t):
        i = get_offset(si)
        j = get_offset(tj)
        c[i] += 1
        c[j] += 1

    ans = "No"

    if len(c.keys()) == 2:
        ans = "Yes"
    else:
        base = c.most_common(1)[0][0]

        others = [key for key in c.keys() if key != base]

        if ((base + 1) % 5 in others) and ((base - 1) % 5 in others):
            ans = "Yes"
        elif ((base + 2) % 5 in others) and ((base - 2) % 5 in others):
            ans = "Yes"

    print(ans)


if __name__ == "__main__":
    main()
