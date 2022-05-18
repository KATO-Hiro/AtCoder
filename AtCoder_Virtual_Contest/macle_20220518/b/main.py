# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    q = int(input())
    two_count = 0  # ti == 2となる回数

    for i in range(q):
        ti, ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        if ti == 1:
            if two_count % 2 == 1:
                # sの並び順はそのままで、インデックスを読みかえる
                if ai < n:
                    ai += n
                else:
                    ai -= n
                if bi < n:
                    bi += n
                else:
                    bi -= n

            s[ai], s[bi] = s[bi], s[ai]
        else:
            two_count += 1

    if two_count % 2 == 1:
        s = s[n:] + s[:n]
    
    print(''.join(s))


if __name__ == "__main__":
    main()
