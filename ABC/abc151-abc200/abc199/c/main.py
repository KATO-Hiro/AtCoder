# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list(input())
    q = int(input())
    two_count = 0

    for i in range(q):
        ti, ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        if ti == 2:
            two_count += 1

        if ti == 1:
            if two_count % 2 == 1:
                if ai <= n - 1:
                    ai += n
                else:
                    ai -= n

                if bi <= n - 1:
                    bi += n
                else:
                    bi -= n

            x = s[ai]
            y = s[bi]

            s[ai] = y
            s[bi] = x

    ans = s

    if two_count % 2 == 1:
        ans = s[n:] + s[:n]

    print("".join(map(str, ans)))


if __name__ == "__main__":
    main()
