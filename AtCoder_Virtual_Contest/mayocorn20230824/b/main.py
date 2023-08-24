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
    u = [get_offset(ui, "a") for ui in "atcoder"]

    # print(u)

    count_s = [0] * 27
    count_t = [0] * 27

    for si, ti in zip(s, t):
        if si == "@":
            count_s[-1] += 1
        else:
            count_s[get_offset(si, "a")] += 1

        if ti == "@":
            count_t[-1] += 1
        else:
            count_t[get_offset(ti, "a")] += 1

    # print(count_s)
    # print(count_t)
    ans = "Yes"

    for i, (cs, ct) in enumerate(zip(count_s, count_t)):
        if i in u:
            diff = ct - cs

            if diff > 0:
                if diff > count_s[-1]:
                    ans = "No"
                    break
                else:
                    count_s[-1] -= diff
            elif diff < 0:
                if abs(diff) > count_t[-1]:
                    ans = "No"
                    break
                else:
                    count_t[-1] -= abs(diff)
        else:
            if cs != ct:
                ans = "No"
                break

    print(ans)


if __name__ == "__main__":
    main()
