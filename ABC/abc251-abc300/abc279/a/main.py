# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    ans = s.count("v") + s.count("w") * 2
    print(ans)
    

if __name__ == "__main__":
    main()
