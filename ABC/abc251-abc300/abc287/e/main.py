# -*- coding: utf-8 -*-


class TrieTree:
    def __init__(self) -> None:
        self.tree = {}
        self.count = 0
    
    def insert(self, word) -> None:
        node = self

        for character in word:
            node.count += 1

            if character not in node.tree:
                node.tree[character] = TrieTree()
            
            node = node.tree[character]
        
        node.count += 1
    
    def calc_longest_common_prefix_count(self, word) -> int:
        node = self
        ans = 0

        for character in word:
            node = node.tree[character]

            if node.count == 1:
                break

            ans += 1

        return ans


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    t = TrieTree()

    for si in s:
        t.insert(si)
    
    for si in s:
        print(t.calc_longest_common_prefix_count(si))


if __name__ == "__main__":
    main()
