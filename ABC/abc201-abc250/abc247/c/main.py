# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    def dfs(count, numbers):
        if count == n:
            return numbers
        
        return dfs(count + 1, numbers + [count + 1] + numbers)
    
    print(*dfs(1, [1]))


if __name__ == "__main__":
    main()
