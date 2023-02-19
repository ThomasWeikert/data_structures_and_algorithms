from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = []
        if self.is_word:
            suffixes.append(suffix)
        for char in self.children:
            suffixes.extend(self.children[char].suffixes(suffix + char))
        return suffixes

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f, prefix='')
