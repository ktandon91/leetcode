class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None :
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.end_of_string = True

    def search(self, word: str) -> bool:
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if node.end_of_string:
            self.res = True
            return
        c = word[0]
        if c == ".":
            for ch in node.children:
                new_node = node.children.get(ch)
                self.dfs(new_node, word[1:])
        else:
            new_node = node.children.get(c, None)
            if new_node is None:
                self.res = False
                return
            self.dfs(new_node, word[1:])

wordDictionary = WordDictionary()
wordDictionary.addWord("BAD")
wordDictionary.addWord("MAD")
wordDictionary.addWord("PAD")
print(wordDictionary.search("P.."))
