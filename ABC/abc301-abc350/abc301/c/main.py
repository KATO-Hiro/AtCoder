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
    x = [0] * 26
    y = [0] * 26
    u = ["a", "t", "c", "o", "d", "e", "r"]
    v = [get_offset(ui, "a") for ui in u]

    for si, ti in zip(s, t):
        if si == "@":
            x[-1] += 1
        else:
            x[get_offset(si, "a")] += 1

        if ti == "@":
            y[-1] += 1
        else:
            y[get_offset(ti, "a")] += 1

    for i, (xi, yi) in enumerate(zip(x, y)):
        if xi == yi:
            continue

        if xi > yi:
            if i in v:
                d = xi - yi

                if y[-1] >= d:
                    y[-1] -= d
                else:
                    print("No")
                    exit()
            else:
                print("No")
                exit()
        elif xi < yi:
            if i in v:
                d = yi - xi

                if x[-1] >= d:
                    x[-1] -= d
                else:
                    print("No")
                    exit()
            else:
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
