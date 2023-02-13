I implemented a blockchain by creating a linked list of blocks, where each block contains data, a timestamp, the hash of the 
previous block, and its own hash calculated using the sha256() function from the hashlib library. The blocks are linked together 
through the nodes in the linked list, with each node pointing to the previous one instead of the next one. The blockchain is 
created using the Blockchain class, which links all the nodes together.

The time it takes to create this chain is proportional to the number of blocks, O(n), where n is the number of blocks. The space 
complexity is also proportional to the size of the data, O(n), as a hash of all the data is generated for each block.