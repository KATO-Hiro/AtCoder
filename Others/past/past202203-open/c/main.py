# -*- coding: utf-8 -*-


def add_offset_to_alphabet(offset: int, base_alphabet: str = 'A') -> str:
    '''Add offset to the base_alphabet.
    Args:
        offset: Difference from the base alphabet. 
        base_alphabet: The base alphabet to use.
    Returns:
        Corrected alphabet.
    
    See:
    https://docs.python.org/3.11/library/functions.html?highlight=chr#ord
    '''   

    return chr(ord(base_alphabet) + offset)


def main():
    import sys

    input = sys.stdin.readline

    alpha = input().rstrip()
    n = len(alpha)
    p, q = divmod(n, 3)

    if q == 0:
        p -= 1
        q += 3
    
    s = add_offset_to_alphabet(p - 1, 'a')
    print(alpha[:q] + s)


if __name__ == "__main__":
    main()
