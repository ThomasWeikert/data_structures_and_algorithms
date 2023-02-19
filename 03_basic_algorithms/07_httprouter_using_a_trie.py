class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.root_handler = root_handler

    def insert(self, path, handler):
        node = self.root
        for part in path:
            node = node.children.setdefault(part, RouteTrieNode())
        node.handler = handler

    def find(self, path):
        node = self.root
        for part in path:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler if node.handler is not None else self.root_handler


class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        handler = self.trie.find(self.split_path(path))
        return handler if handler is not None else self.not_found_handler

    def split_path(self, path):
        parts = path.split('/')
        return [p for p in parts if p]  # remove empty strings (e.g. from trailing slash)

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'
