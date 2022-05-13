# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)

    if s == "keyence":
        print("YES")
        exit()

    for size in range(1, n):
        for i in range(n - size + 1):
            t = s[:i] + s[i + size:]

            if t == "keyence":
                print("YES")
                exit()
    
    print("NO")


if __name__ == "__main__":
    main()
