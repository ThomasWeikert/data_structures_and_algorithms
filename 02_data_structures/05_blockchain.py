import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash, next=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = next

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        hash_str = hash_str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, block):
        if self.head is None:
            self.head = block
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = block

class Blockchain:
    def __init__(self):
        self.blockchain = LinkedList()
        self.blockchain.append(Block("0", "Genesis Block", "0"))

    def add_block(self, data):
        last_block = self.blockchain.head
        while last_block.next:
            last_block = last_block.next
        self.blockchain.append(Block(time.time(), data, last_block.hash))

# Test cases
blockchain = Blockchain()

# Test Case 1
blockchain.add_block("Transaction Data 1")
assert blockchain.blockchain.head.next.data == "Transaction Data 1"

# Test Case 2
blockchain.add_block("Transaction Data 2")
assert blockchain.blockchain.head.next.next.data == "Transaction Data 2"

# Test Case 3 (Edge Case)
blockchain.add_block("")
assert blockchain.blockchain.head.next.next.next.data == ""
