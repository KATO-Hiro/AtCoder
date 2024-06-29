# -*- coding: utf-8 -*-


# See:
# https://atcoder.jp/contests/abc353/submissions/53334275
class TrieTree:
    def __init__(self) -> None:
        self.tree = {}
        self.count = 0

    def insert(self, word: str) -> int:
        node = self
        ans = 0

        for character in word:
            if character not in node.tree:
                node.tree[character] = TrieTree()

            node = node.tree[character]
            ans += node.count
            node.count += 1

        return ans


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(map(str, input().split()))
    t = TrieTree()
    ans = 0

    for si in s:
        ans += t.insert(si)

    print(ans)


if __name__ == "__main__":
    main()
