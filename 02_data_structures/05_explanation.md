**Implementation**

The implementation is a simple blockchain using a singly linked list to store the blocks.

- A block is represented by the Block class, which has four attributes: timestamp, data, previous_hash, and hash.
- The calc_hash() method is used to generate the hash value for the block using the SHA-256 algorithm.
- A linked list of blocks is maintained by the LinkedList class.
- A blockchain is represented by the Blockchain class which maintains the linked list of blocks.
- The add_block() method is used to add new blocks to the blockchain. Each new block is linked to the previous block by storing the hash of the previous block in the previous_hash attribute.
- The print_blockchain() method is used to print the contents of the blockchain. It iterates through the linked list and prints the timestamp, data, and hash value of each block.
- The program includes a run_blockchain_tests() function that defines three test cases to test the functionality of the blockchain. The first test case adds three blocks to the blockchain and checks the expected output against the actual output. The second test case checks the expected output when an empty blockchain is printed. The third test case checks the expected output when an empty block is added to the blockchain.

**Time and space complexity**
The time and space complexity of the implementation are as follows:

- __init__ method for both HashTable and Node classes have a time complexity of O(1) since they only initialize a few variables.

- add method for HashTable has a time complexity of O(1) on average, but could be O(n) in the worst case if there are many hash collisions, where n is the number of items in the table. The space complexity for this method is also O(1) on average, but could be up to O(n) in the worst case.

- get method for HashTable has a time complexity of O(1) on average for a successful lookup. In the worst case, the time complexity can be O(n) if all items have the same hash value or when there are many collisions, where n is the number of items in the table. The space complexity for this method is O(1) since it only returns the value for a given key.

- remove method for HashTable has a time complexity of O(1) on average, but could be O(n) in the worst case if there are many collisions or if the item to be removed is at the end of a long linked list. The space complexity for this method is also O(1) since it only removes the item for a given key.

Overall, the time complexity of the implementation is on average O(1) for adding, getting, and removing items from the hash table. The worst-case time complexity can be O(n) if there are many hash collisions, but this is unlikely if the hash function is well-designed. The space complexity is also O(n), where n is the number of items in the table, but it is usually much lower in practice.
