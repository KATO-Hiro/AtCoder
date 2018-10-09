# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    v = list(map(int, input().split()))

    if len(set(v)) == 1:
        print(n // 2)
        exit()
    else:
        even = Counter(v[::2]).most_common(1)[0][0]
        odd = Counter(v[1::2]).most_common(1)[0][0]
        ans1 = 0

        if even == odd:
            even2 = Counter(v[::2]).most_common(2)[1][0]
            odd2 = Counter(v[1::2]).most_common(2)[1][0]
            ans2 = 0
            ans3 = 0

            for x in range(n):
                if x % 2 == 0:
                    if v[x] != even:
                        ans2 += 1
                else:
                    if v[x] != odd2:
                        ans2 += 1

            for y in range(n):
                if y % 2 == 0:
                    if v[y] != even2:
                        ans3 += 1
                else:
                    if v[y] != odd:
                        ans3 += 1

            print(min(ans2, ans3))
            exit()

        for i in range(n):
            if i % 2 == 0:
                if v[i] != even:
                    ans1 += 1
            else:
                if v[i] != odd:
                    ans1 += 1

        print(ans1)


if __name__ == '__main__':
    main()
