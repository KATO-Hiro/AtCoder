# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    s = s.replace("00", "0")
    print(len(list(s)))
    

if __name__ == "__main__":
    main()
