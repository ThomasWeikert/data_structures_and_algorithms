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
            block.next = None  # set the next attribute of the new block to None
        print("Block added with data:", block.data, "and hash:", block.hash)

class Blockchain:
    def __init__(self):
        self.blockchain = LinkedList()
        self.blockchain.append(Block("0", "Genesis Block", "0"))

    def add_block(self, data):
        if self.blockchain.head is None:
            self.blockchain.append(Block(time.time(), data, self.blockchain.head.hash))
        else:
            last_block = self.blockchain.head
            while last_block.next:
                last_block = last_block.next
            self.blockchain.append(Block(time.time(), data, last_block.hash))

    def print_blockchain(self):
        current = self.blockchain.head
        result = ""
        while current:
            result += f"Timestamp: {current.timestamp}, Data: {current.data}, Hash: {current.hash}\n"
            current = current.next
        return result

def run_blockchain_tests():
    # Test Case 1
    print('************************************************ Test Case 1')
    blockchain = Blockchain()
    blockchain.add_block("Transaction 1")
    blockchain.add_block("Transaction 2")
    blockchain.add_block("Transaction 3")
    blockchain.print_blockchain()
    expected_output = [
                       f"Timestamp: 0, Data: Genesis Block, Hash: {blockchain.blockchain.head.hash}\n",
                       f"Timestamp: {blockchain.blockchain.head.next.timestamp}, Data: Transaction 1, Hash: {blockchain.blockchain.head.next.hash}\n",
                       f"Timestamp: {blockchain.blockchain.head.next.next.timestamp}, Data: Transaction 2, Hash: {blockchain.blockchain.head.next.next.hash}\n",
                       f"Timestamp: {blockchain.blockchain.head.next.next.next.timestamp}, Data: Transaction 3, Hash: {blockchain.blockchain.head.next.next.next.hash}\n"
    ]
    actual_output = blockchain.print_blockchain()
    for i in range(len(expected_output)):
        print("Actual output: " + "\n" + str(actual_output.splitlines()[i]))
        print("Expected output: " + "\n" + str(expected_output[i]))


    # Test Case 2 (Edge Case)
    print('************************************************ Test Case 2')
    blockchain = Blockchain()
    blockchain.print_blockchain()
    expected_output = [f"Timestamp: 0, Data: Genesis Block, Hash: {blockchain.blockchain.head.hash}\n"]
    actual_output = blockchain.print_blockchain()
    for i in range(len(expected_output)):
        print("Actual output: " + "\n" + str(actual_output.splitlines()[i]))
        print("Expected output: " + "\n" + str(expected_output[i]))


    # Test Case 3 (Edge Case)
    print('************************************************ Test Case 3')
    blockchain = Blockchain()
    blockchain.add_block("")
    blockchain.print_blockchain()
    expected_output = [
                       f"Timestamp: 0, Data: Genesis Block, Hash: {blockchain.blockchain.head.hash}\n",
                       f"Timestamp: {blockchain.blockchain.head.next.timestamp}, Data: Transaction 1, Hash: {blockchain.blockchain.head.next.hash}\n",
    ]
    actual_output = blockchain.print_blockchain()
    for i in range(len(expected_output)):
        print("Actual output: " + "\n" + str(actual_output.splitlines()[i]))
        print("Expected output: " + "\n" + str(expected_output[i]))

run_blockchain_tests()
