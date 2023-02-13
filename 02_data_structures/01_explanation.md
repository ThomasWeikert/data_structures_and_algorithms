To efficiently retrieve cache data, I chose to use a dictionary data structure. The use of key-value pairs allows me to retrieve 
values in constant time, O(1), which reduces the time complexity. Additionally, I used a double-linked list to enqueue and 
dequeue nodes, with each node pointing both forward and backward. I also stored the head and tail nodes of the linked list to 
simplify accessing them.

The time complexity for accessing values is O(1) since both accessing values in a dictionary and getting the stored values of 
the first and last elements in a linked list are O(1). However, setting the data has a time complexity of O(n), where n is the 
number of data points being set. Retrieving the data is once again O(1), through the use of the dictionary.

The space complexity for setting data is O(n), and the space complexity for retrieving data is O(1).
