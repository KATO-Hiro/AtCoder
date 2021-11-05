# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a1 = a[0]
    b = list()

    for ai in a:
        if ai == -1:
            b.append(a1)
        else:
            b.append(ai)
    
    if sorted(b)[n - 1] == a1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
