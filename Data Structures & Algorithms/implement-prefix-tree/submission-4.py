class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr_node.children[idx]:
                curr_node.children[idx] = TrieNode()
            curr_node = curr_node.children[idx]

        curr_node.is_end = True
        return


    def search(self, word: str) -> bool:
        curr_node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr_node.children[idx]:
                return False
            curr_node = curr_node.children[idx]

        return curr_node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not curr_node.children[idx]:
                return False
            curr_node = curr_node.children[idx]

        return True
        
        