# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() * (n + 1) for _ in range(n)]
    ans = float("inf")

    for number in range(10):
        used = [False] * n
        candidate = float("inf")
        count = 0

        for t in range(len(s[0])):
            used_number = set()

            for i in range(n):
                value = s[i][t]

                if not used[i] and value not in used_number and value == str(number):
                    used[i] = True
                    count += 1
                    used_number.add(value)
        
            if count == n:
                candidate = t
                break

        ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
