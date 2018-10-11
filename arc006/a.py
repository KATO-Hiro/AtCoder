# -*- coding: utf-8 -*-


def main():
    e = list(map(int, input().split()))
    b = int(input())
    l = list(map(int, input().split()))

    matched_count = len(set(e) & set(l))

    if matched_count == 6:
        print(1)
    elif matched_count == 5:
        if b in l:
            print(2)
        else:
            print(3)
    elif matched_count == 4:
        print(4)
    elif matched_count == 3:
        print(5)
    else:
        print(0)


if __name__ == '__main__':
    main()
