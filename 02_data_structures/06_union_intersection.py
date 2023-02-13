class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Create a set to store the values in the first linked list
    set_1 = set()
    node = llist_1.head
    while node:
        set_1.add(node.value)
        node = node.next
    
    # Create a set to store the values in the second linked list
    set_2 = set()
    node = llist_2.head
    while node:
        set_2.add(node.value)
        node = node.next
    
    # Union of the two sets
    union_set = set_1.union(set_2)
    
    # Create a linked list to store the union of the two linked lists
    union_linked_list = LinkedList()
    for value in union_set:
        union_linked_list.append(value)
    
    return union_linked_list


def intersection(llist_1, llist_2):
    # Create a set to store the values in the first linked list
    set_1 = set()
    node = llist_1.head
    while node:
        set_1.add(node.value)
        node = node.next
    
    # Create a set to store the values in the second linked list
    set_2 = set()
    node = llist_2.head
    while node:
        set_2.add(node.value)
        node = node.next
    
    # Intersection of the two sets
    intersection_set = set_1.intersection(set_2)
    
    # Create a linked list to store the intersection of the two linked lists
    intersection_linked_list = LinkedList()
    for value in intersection_set:
        intersection_linked_list.append(value)
    
    return intersection_linked_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("\nTest case Udacity1:")
print("Union:", union(linked_list_1, linked_list_2))
print("Intersection:", intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("\nTest case Udacity2:")
print("Union:", union(linked_list_3, linked_list_4))
print("Intersection:", intersection(linked_list_3, linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test case 1: Normal case with common elements
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [0,7,43,35,6,11,28,63,21]
element_2 = [6,32,4,9,6,1,11,21,63]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("\nMy test case 1:")
print("Union:", union(linked_list_1, linked_list_2))
print("Intersection:", intersection(linked_list_1, linked_list_2))

# Test case 2: Edge case with large values
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [i for i in range(106)]
element_2 = [i for i in range(106, 2*10**6)]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("\nTest case 2:")
print("Union:", union(linked_list_7, linked_list_8))
print("Intersection:", intersection(linked_list_7, linked_list_8))

# Test case 3: Edge case with empty linked lists
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print("\nMy test case 3:")
print("Union:", union(linked_list_5, linked_list_6))
print("Intersection:", intersection(linked_list_5, linked_list_6))

