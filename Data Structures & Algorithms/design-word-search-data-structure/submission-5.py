class TreeNode():
    def __init__(self):
        self.hm = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        
        for w in word:
            if w in curr.hm:
                curr = curr.hm[w]
            else:
                curr.hm[w] = TreeNode()
                curr = curr.hm[w]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root



        def dfs(curr, i):
            if i == len(word) and curr.end:
                return True
            if i == len(word) - 1 and curr.hm and word[i] == "." and curr.end:
                return True

            if i == len(word):
                return False

            
            if word[i] in curr.hm:
                return dfs(curr.hm[word[i]], i + 1)
            elif word[i] == ".":
                for key in curr.hm:
                    if dfs(curr.hm[key], i + 1):
                        return True
                return False
            else:
                return False


        
        return dfs(self.root, 0)
