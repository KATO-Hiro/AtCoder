# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = set()
    ans.add(0)

    for pi in p:
        candidates = list()

        for a in ans:
            candidates.append(a + pi)

        for candidate in candidates:
            ans.add(candidate)

    print(len(ans))


if __name__ == '__main__':
    main()
