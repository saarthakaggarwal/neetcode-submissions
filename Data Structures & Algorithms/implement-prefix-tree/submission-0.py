class TreeNode:
    def __init__(self, val):
        self.val = val
        self.hm = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode(val = "")

    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w in curr.hm:
                curr = curr.hm[w]
            else:
                curr.hm[w] = TreeNode(f"{w}")
                curr = curr.hm[w]
        curr.end = True 

    def search(self, word: str) -> bool:
        curr = self.root

        for w in word:
            if w in curr.hm:
                curr = curr.hm[w]
            else:
                return False

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for w in prefix:
            if w in curr.hm:
                curr = curr.hm[w]
            else:
                return False
        
        return True