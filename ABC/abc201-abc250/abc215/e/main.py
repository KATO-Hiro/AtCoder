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

    n = int(input())
    s = input().rstrip()
    types = 10
    patterns = 1 << types
    dp = [[0] * types for _ in range(patterns)]
    mod = 998244353

    for i in range(n):
        cur = get_offset(s[i])

        for pattern in reversed(range(patterns)):
            for prev in range(types):
                if pattern >> prev & 1:
                    if cur == prev:
                        dp[pattern][prev] += dp[pattern][prev]
                        dp[pattern][prev] %= mod  
                        
                    if ~pattern >> cur & 1:
                        dp[pattern | 1 << cur][cur] += dp[pattern][prev]
                        dp[pattern | 1 << cur][cur] %= mod
                    
        dp[1 << cur][cur] += 1
        dp[1 << cur][cur] %= mod
        
        dp = dp
    
    ans = 0
    
    for d in dp:
        ans += sum(d)
        ans %= mod

    print(ans)
    

if __name__ == "__main__":
    main()
