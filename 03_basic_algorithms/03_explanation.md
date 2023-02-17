As I am not allowed to use any sorting built in functions from python, I can implement a sorting algorithm myself. One such algorithm is merge sort, which has a time complexity of O(n log n).


**Concept:**
Merge sort is a divide-and-conquer sorting algorithm that works by dividing the input list into two halves, recursively sorting each half, and then merging the two sorted halves back into a single sorted list. Here's how the algorithm works:

Divide: If the input list has length 0 or 1, it is already sorted. Otherwise, divide the list into two halves, left and right.

Conquer: Recursively sort the left and right halves using merge sort.

Combine: Merge the two sorted halves back into a single sorted list. To do this, compare the first elements of the two lists, and choose the smaller one to be the next element in the merged list. Repeat this process until one of the two lists is empty, and then add the remaining elements of the other list to the end of the merged list.

The key idea of merge sort is that it sorts a list by recursively dividing it into smaller and smaller pieces until the pieces are trivially sorted (i.e., lists of length 0 or 1), and then merging those pieces back together in a sorted order. This approach allows merge sort to achieve a time complexity of O(n log n), which is faster than most other sorting algorithms for large lists.

One of the main advantages of merge sort is that it is a stable sorting algorithm, which means that it preserves the relative order of equal elements in the input list. This property can be important in some applications. Another advantage is that merge sort can be easily parallelized, since the sorting and merging of the two halves can be performed independently.

**Example:**
Let's take the example of the input list ```[38, 27, 43, 3, 9, 82, 10]``` and see how the merge sort algorithm would sort it.

Divide the input list into two halves:
```[38, 27, 43, 3]  [9, 82, 10]```

Recursively sort the two halves using merge sort:

```[38, 27, 43, 3] -> [38, 27]  [43, 3]```
```[9, 82, 10]     -> [9]  [82, 10]```

Recursively sort the two halves using merge sort:
```[38, 27] -> [27]  [38]```
```[43, 3]  -> [3]  [43]```
```[82, 10] -> [82]  [10]```

Merge the two sorted halves into a single sorted list using the merge function:
```[27]  [38]  -> [27, 38]```
```[3]  [43]   -> [3, 43]```
```[82]  [10]  -> [10, 82]```

```[27, 38]  [3, 43]   -> [3, 27, 38, 43]```
```[9]       [10, 82]  -> [9, 10, 82]```

Merge the two sorted halves into a single sorted list using the merge function:
```[3, 27, 38, 43]  [9, 10, 82]  -> [3, 9, 10, 27, 38, 43, 82]```

And that's it! The input list ```[38, 27, 43, 3, 9, 82, 10]``` is sorted in ascending order using merge sort in O(n log n) time complexity.

**Reverse parameter:**
The reverse parameter in both merge_sort and merge functions is used to control the order in which the elements are sorted.

When reverse is set to False, the sorting is done in ascending order, which is the default behavior. For example, if the input list is [5, 2, 8, 1, 4], the sorted list will be [1, 2, 4, 5, 8].

When reverse is set to True, the sorting is done in descending order. For example, if the input list is [5, 2, 8, 1, 4] and reverse=True, the sorted list will be [8, 5, 4, 2, 1].

In the rearrange_digits function, we set reverse=True to sort the input list in descending order so that we can divide it into two parts with the highest digits at the beginning of each part. This ensures that we get the maximum possible sum when we concatenate the digits of each part to form the two numbers.



