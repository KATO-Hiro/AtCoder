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
    from string import ascii_uppercase
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    alpha = ascii_uppercase * 2
    ans = list()

    for si in s:
        index = get_offset(si)
        index += n

        ans.append(alpha[index])
    
    print(''.join(ans))


if __name__ == "__main__":
    main()
