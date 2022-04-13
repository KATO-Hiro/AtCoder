# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    ans = 0

    for i in range(101):
        tmp = []

        for index, hi in enumerate(h):
            if hi != 0:
                tmp.append((hi, index))
            else:
                if len(tmp) > 0:
                    candidate = float('inf')

                    for hi, index in tmp:
                        candidate = min(candidate, hi)

                    for hi, index in tmp:
                        h[index] -= int(candidate)

                    ans += candidate

                tmp = []
            
        if len(tmp) > 0:
            candidate = float('inf')

            for hi, index in tmp:
                candidate = min(candidate, hi)

            for hi, index in tmp:
                h[index] -= int(candidate)

            ans += candidate

    print(ans)


if __name__ == "__main__":
    main()
