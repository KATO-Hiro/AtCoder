# -*- coding: utf-8 -*-


def main():
    from string import ascii_lowercase

    p = list(map(int, input().split()))
    ans = ''

    for pi in p:
        ans += ascii_lowercase[pi - 1]
    
    print(ans)


if __name__ == "__main__":
    main()
