# -*- coding: utf-8 -*-


def main():
    e = list(map(int, input().split()))
    b = int(input())
    l = list(map(int, input().split()))

    matched_count = len(set(e) & set(l))

    # See:
    # https://beta.atcoder.jp/contests/arc006/submissions/3183342
    if matched_count == 6:
        print(1)
    elif matched_count == 5 and b in l:
        print(2)
    elif matched_count >= 3:
        print(8 - matched_count)
    else:
        print(0)


if __name__ == '__main__':
    main()
