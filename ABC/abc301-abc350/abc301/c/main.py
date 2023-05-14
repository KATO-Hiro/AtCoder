# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    cs = Counter(s)
    ct = Counter(t)

    for ci in "atcoder":
        u = max(cs[ci], ct[ci])

        # @だけでは、同じにできない
        if cs["@"] < u - cs[ci] or ct["@"] < u - ct[ci]:
            print("No")
            exit()

        # 差分を@で補う
        cs["@"] -= u - cs[ci]
        cs[ci] = u
        ct["@"] -= u - ct[ci]
        ct[ci] = u

    if cs == ct:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
