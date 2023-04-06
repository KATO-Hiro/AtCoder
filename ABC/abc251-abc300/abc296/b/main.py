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

    s = [list(input().rstrip()) for _ in range(8)]

    for i in range(7, -1, -1):
        for j in range(8):
            if s[i][j] == "*":
                j = add_offset_to_alphabet(j, "a")
                print(j + str(8 - i))
                exit()
    

if __name__ == "__main__":
    main()
