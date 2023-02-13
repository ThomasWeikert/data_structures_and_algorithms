To encode the string for this problem, I looped through each character and counted the number of occurrences, storing these 
values in a dictionary. I used a heap to store the occurrences of characters in the string.

The time complexity for huffman encoding is O(n log(n)), where n is the number of unique characters in the input data.

For decoding, I expanded on the values I stored in the encoding step. The runtime complexity for both encoding and decoding the 
data is O(n^2), where n is the number of characters, as I looped through twice, first to count and then to store the 
occurrences.

The time complexity of huffman decoding is O(n), where n is the length of the input data.

The space complexity for encoding is O(n * log(n)), while the space complexity for decoding is O(n).
