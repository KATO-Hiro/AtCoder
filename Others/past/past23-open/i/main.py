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

    n, y = map(int, input().split())
    sx = []

    for _ in range(n):
        si, xi = map(str, input().split())
        ti = 0

        for sij in si:
            ti |= 1 << get_offset(sij, "a")

        sx.append((ti, int(xi)))

    ans = 0

    for bit in range(1 << n):
        cost = 0
        t = 0

        for i in range(n):
            if bit & (1 << i):
                ti, xi = sx[i]

                t |= ti
                cost += xi

        if cost > y:
            continue

        ans = max(ans, bin(t).count("1"))

    print(ans)


if __name__ == "__main__":
    main()
