# -*- coding: utf-8 -*-


def main():
    from itertools import product
    from collections import Counter
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(h)]

    patterns = product([0, 1], repeat=h)
    ans = 1

    for pattern in patterns:
        indices = [index for index, p in enumerate(pattern) if p == 1]

        if len(indices) == 0:
            continue

        numbers = list()
    
        for wi in range(w):
            number = set()

            for index in indices:
                number.add(p[index][wi])
            
            if len(number) == 1:
                numbers.append(list(number)[0])

        freq = Counter(numbers).most_common()

        if len(freq) >= 1:
            ans = max(ans, freq[0][1] * len(indices))

    print(ans)


if __name__ == "__main__":
    main()
