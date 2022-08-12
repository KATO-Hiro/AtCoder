# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    w1 = input().rstrip()

    s = set()
    s.add(w1)
    before = w1[-1]

    for _ in range(n - 1):
        wi = input().rstrip()

        if wi in s:
            print('No')
            exit()
        else:
            if before != wi[0]:
                print('No')
                exit()
        
        s.add(wi)
        before = wi[-1]
    
    print("Yes")


if __name__ == "__main__":
    main()
