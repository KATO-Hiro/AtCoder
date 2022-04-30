# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = input().rstrip()

    if len(set(list(x))) == 1:
        print("Weak")
        exit()
    
    count = 0
    
    for j, k in zip(x, x[1:]):
        if (int(j) + 1) % 10 == int(k):
            count += 1
    
    if count == 3:
        print("Weak")
    else:
        print("Strong")


if __name__ == "__main__":
    main()
