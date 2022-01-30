# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    m = int(input())
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}

    for i in range(m):
        s = input().rstrip()

        result = ""

        for si in s:
            result = d[si] + result
        
        print(result)



if __name__ == "__main__":
    main()
