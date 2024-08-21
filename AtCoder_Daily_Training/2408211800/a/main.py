# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    ans = "Strong"

    if len(set(list(s))) == 1:
        ans = "Weak"
    else:
        ok = True

        for i in range(3):
            si, sj = int(s[i]), int(s[i + 1])

            if (si + 1) % 10 != sj:
                ok = False
                break

        if ok:
            ans = "Weak"

    print(ans)


if __name__ == "__main__":
    main()
