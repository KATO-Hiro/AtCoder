# -*- coding: utf-8 -*-


def get_offset(alphabet: str, base_alphabet: str = 'A') -> int:
    '''Get offset between the base_alphabet and alphabet.
    Args:
        alphabet: The alphabet to use. 
        base_alphabet: The base alphabet to use.
    Returns:
        difference between the base_alphabet and alphabet.
    
    See:
    https://docs.python.org/3.11/library/functions.html?highlight=chr#ord
    '''   

    return ord(alphabet) - ord(base_alphabet)


def solve():
    from math import ceil

    n = int(input())
    s = input().rstrip()
    size = ceil(n / 2)
    mod = 998244353
    ans = 0

    for i in range(size):
        x = get_offset(s[i])
        ans += pow(26, size - i - 1, mod) * x
    
    if n % 2 == 0:
        t = s[:size] + s[:size][::-1]
    else:
        t = s[:size] + s[:size - 1][::-1]

    if t <= s:
        ans += 1
    
    print(ans % mod)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for i in range(t):
        solve()


if __name__ == "__main__":
    main()
