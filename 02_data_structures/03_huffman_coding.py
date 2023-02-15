import sys

def huffman_encoding(data):
    if data is None:
        return ("No data to encode"), None

    count = {}

    for i in data:
        if i in count.keys():
            count[i] += 1
        else:
            count.update({i: 1})

    vals = {}
    bc = '1'
    for c in sorted(count.items()):
        vals[c[0]] = bc
        bc = '0' + bc

    encode = ''
    for d in data:
        encode += vals[d]

    return encode, vals


def huffman_decoding(data,tree):
    if tree is None:
        return ("No data to decode")

    vals = {}

    for t in tree:
        vals[tree[t]] = t
    bc = ''
    decode = ''
    for d in data:
        if d == '1':
            decode += vals[bc + d]
            bc = ''
        else:
            bc += d

    return decode

def test_huffman_encoding_and_decoding():
    # Test case 1: Null input
    data = None
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == "No data to decode", f"Expected No data to decode, but got {decoded_data}"

    # Test case 2: Empty input
    data = ""
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == data, f"Expected {data}, but got {decoded_data}"

    # Test case 3: Large input
    data = "A" * 10000
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == data, f"Expected {data}, but got {decoded_data}"

    # Test case 4
    data = "The quick brown fox jumps over the lazy dog"
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == data, f"Expected {data}, but got {decoded_data}"

    # Test case 5
    data = "This is an example of a huffman tree"
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == data, f"Expected {data}, but got {decoded_data}"

    # Test case 5
    data = "huffman coding is lossless"
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == data, f"Expected {data}, but got {decoded_data}"

    return print("success")



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    #print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    #print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #print ("The content of the encoded data is: {}\n".format(decoded_data))


    test_huffman_encoding_and_decoding()