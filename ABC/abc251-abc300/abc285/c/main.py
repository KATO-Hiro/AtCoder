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


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())[::-1]
    p = 1
    ans = 0

    for si in s:
        index = get_offset(si) + 1
        ans += index * p

        p *= 26

    print(ans)
    

if __name__ == "__main__":
    main()
