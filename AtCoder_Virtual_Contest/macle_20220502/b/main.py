# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    ans = ""

    for si in s:
        if si == "1":
            ans += "1"
        elif si == "0":
            ans += "0"
        else:
            if ans == "":
                pass
            else:
                ans = ans[:-1]
    
    print(ans)


if __name__ == "__main__":
    main()
