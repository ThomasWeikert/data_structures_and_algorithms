class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.current_size = 0
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._set_head(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        if self.current_size == self.capacity:
            self._remove_LRU()
        new_node = Node(value)
        self.cache[key] = new_node
        self._set_head(new_node)
        self.current_size += 1
    
    def _set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            node.prev = self.head
            if self.head.prev == None:
                self.tail = self.head
            self.head = node
        
    def _remove_node(self, node):
        if self.current_size == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.prev
            self.head.next = None
        elif node == self.tail:
            self.tail.next.prev = None
            self.tail = self.tail.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
    def _remove_LRU(self):
        node = self.tail
        del self.cache[node.value]
        self._remove_node(node)
        self.current_size -= 1

        
# Tests
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

# Test Case 1
print("************************* Test Case 1:")
cache1 = LRU_Cache(5)
cache1.set(None, None)
cache1.set(2, None)
print(f"get none: {cache1.get(None)}")      # returns None
print(f"get none, key 2: {cache1.get(2)}")      # returns None


# Test Case 2
print("************************* Test Case 2:")
cache2 = LRU_Cache(5)
cache2.set("string", "bla")
print(f"get string: {cache2.get('string')}")      # returns bla
cache2.set(2, 2)
cache2.set("string", 3)
cache2.set(4, 4)
print(f"get string: 3, overwritten: {cache2.get('string')}")      # returns bla

# Test Case 3
print("************************* Test Case 3:")
cache3 = LRU_Cache(3)
cache3.set(1, 1)
cache3.set(2, 2)
cache3.set(3, 3)
cache3.set(4, 4)
print(f"get 4: {cache3.get(4)}")       # returns 4
print(f"get -1 bc we removed it from cache: {cache3.get(1)}")       # returns -1