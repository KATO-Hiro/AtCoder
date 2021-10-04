# -*- coding: utf-8 -*-


def main():
    s = list(input())
    t = list(input())
    n = len(s)

    if s == t:
        print("Yes")
        exit()
    
    for i in range(n - 1):
        s[i], s[i + 1] = s[i + 1], s[i]

        if s == t:
            print("Yes")
            exit()

        s[i], s[i + 1] = s[i + 1], s[i]

    print("No")


if __name__ == "__main__":
    main()
