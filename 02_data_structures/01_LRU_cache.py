class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        elif len(self.cache) >= self.capacity:
            if self.cache:
                oldest = self.order.pop(0)
                self.cache.pop(oldest)
                self.cache[key] = value
                self.order.append(key)
        else:
            self.cache[key] = value
            self.order.append(key)

        
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
