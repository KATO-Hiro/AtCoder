# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    t = input()
    ans = ""

    for index, ti in enumerate(t, 1):
        if index >= k:
            if ti.islower():
                ans += ti.upper()
            else:
                ans += ti.lower()
        else:
            ans += ti

    print(ans)


if __name__ == "__main__":
    main()
