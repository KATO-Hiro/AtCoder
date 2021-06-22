# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    sorted_s = sorted(s, key=lambda x: (int(x), -len(x)))
    print("\n".join(sorted_s))


if __name__ == "__main__":
    main()
