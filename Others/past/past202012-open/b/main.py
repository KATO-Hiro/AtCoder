# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    ans = ""

    for si in s:
        if si in ans:
            ans = ans.replace(si, "")

        ans = ans + si

    print(ans)


if __name__ == "__main__":
    main()
