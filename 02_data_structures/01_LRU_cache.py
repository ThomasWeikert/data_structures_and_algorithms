class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return -1
        self.move_to_head(node)
        return node.value

    def set(self, key, value):
        node = self.cache.get(key)
        if not node:
            node = Node(key, value)
            self.cache[key] = node
            self.add_node(node)
            if len(self.cache) > self.capacity:
                tail = self.remove_tail()
                del self.cache[tail.key]
        else:
            node.value = value
            self.move_to_head(node)

        
# Udacity Tests
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test case 1: Normal functionality
cache = LRU_Cache(2)

cache.set(1, 1)
cache.set(2, 2)

assert cache.get(1) == 1 # returns 1
cache.set(3, 3) # evicts key 2
assert cache.get(2) == -1 # returns -1 (not found)

cache.set(4, 4) # evicts key 1
assert cache.get(1) == -1 # returns -1 (not found)
assert cache.get(3) == 3 # returns 3
assert cache.get(4) == 4 # returns 4

# Test case 2: Edge case - Empty Cache
cache = LRU_Cache(0)

assert cache.get(1) == -1 # returns -1 (not found)
cache.set(1, 1) # does nothing, since the cache is empty
assert cache.get(1) == -1 # returns -1 (not found)

# Test case 3: Edge case - Large Values
cache = LRU_Cache(10**9)

for i in range(10**6):
    cache.set(i, i)

assert cache.get(0) == 0 # returns 0
assert cache.get(10**6-1) == 10**6-1 # returns 10**6-1
