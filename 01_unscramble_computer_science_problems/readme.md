# Time Complexity Analysis


## Task0:
This task will take constant time i.e., O(1) as the access time for items in a list will take a constant time.

## Task1:
This task will take linear time i.e., O(n) as we have to iterate through each line in a list to get phone numbers. Even though there are two for loops (one for texts and another for calls) which will take O(n+n) => O(2n), we can round it off to O(n).

## Task2:
O(n): for the for loop
O(n): for max items in a list
Total time complexity O(n+n) => O(n)

## Task3:
**PartA:**
O(n): for loop takes O(n) time complexity
O(n): max() time complexity
O(nlogn): sorting takes O(nlogn)
Total time complexity: 0(n + n + nlogn) => O(2n + nlogn) => O(nlogn)

**PartB:**
O(n): for loop takes O(n) time complexity
O(n): for loop takes O(n) time complexity
Total time complexity: O(2n) --> 0(n)

## Task4:
O(n): the 4 list comprehensions take O(n) complexity each. O(4n) => O(n)
O(n): for loop takes O(n) time complexity
O(nlogn): sorting takes O(nlogn)
Total time complexity: O(n + n + nlogn) => O(2n + nlogn) => O(nlogn)