# -*- coding: utf-8 -*-


def main():
    s = input()
    t = input()
    n = len(s)

    if s == t:
        print("Yes")
        exit()
    
    for i in range(n - 1):
        ns = s[:i] + s[i + 1] + s[i] + s[i + 2:]

        if ns == t:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
