# -*- coding: utf-8 -*-


def main():
    d1 = {
        "0": "nil",
        "1": "un",
        "2": "bi",
        "3": "tri",
        "4": "quad",
        "5": "pent",
        "6": "hex",
        "7": "sept",
        "8": "oct",
        "9": "enn",
    }

    d2 = {
        "0": "nilium",
        "1": "unium",
        "2": "bium",
        "3": "trium",
        "4": "quadium",
        "5": "pentium",
        "6": "hexium",
        "7": "septium",
        "8": "octium",
        "9": "ennium",
    }

    n = input()
    ans = ""

    if n[0] == "9" and n[1] == "0":
        ans = d1["9"][:2]
        ans += d1["0"]
        ans += d2[n[2]]
    elif n[1] == "9" and n[2] == "0":
        ans = d1[n[0]]
        ans += d1["9"][:2]
        ans += d2["0"]
    else:
        ans = d1[n[0]]
        ans += d1[n[1]]
        ans += d2[n[2]]

    print(ans[0].upper() + ans[1:])


if __name__ == "__main__":
    main()
