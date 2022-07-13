class Trie:

    def __init__(self):
        self.children = dict()
        self.isTerminated = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = Trie()
                curr = curr.children[c]
        curr.isTerminated = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.isTerminated
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)