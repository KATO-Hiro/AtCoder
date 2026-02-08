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
    from atcoder import fenwicktree

    input = sys.stdin.readline

    n, q = map(int, input().split())
    s = input().rstrip()
    t = [get_offset(si, "a") for si in s]
    size = n + 10
    bits = [fenwicktree.FenwickTree(size) for _ in range(26)]

    for i, ti in enumerate(t):
        bits[ti].add(i, 1)

    ans = list()

    for _ in range(q):
        query = list(map(str, input().split()))

        if query[0] == "1":
            p, c = query[1:]
            p = int(p) - 1
            cur = get_offset(c, "a")

            prev = t[p]
            bits[prev].add(p, -1)

            bits[cur].add(p, 1)
            t[p] = cur
        else:
            l, r = query[1:]
            l, r = int(l) - 1, int(r)
            candidate = 0

            for bit in bits:
                now = bit.sum(l, r)
                candidate = max(candidate, now)

            ans.append(candidate)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
