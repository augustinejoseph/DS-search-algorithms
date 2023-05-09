# Search Algorithms in DSA

## Linear Search
The function linearSearch takes two arguments - an array (arr) and a target element to search for (target). The function iterates over each element of the array using a for loop and checks if the current element is equal to the target element. If the target element is found, the index of the element is returned. If the entire array is searched and the target element is not found, False is returned.

In the given code, an array [1,2,3,4,5,6,7,8,9] is defined and the target element to search for is 2. The linearSearch function is called with these two arguments and the returned index is printed. If the returned value is not False, the element found and its index are printed. Otherwise, "Not found" is printed.

In this implementation, the time complexity of the linear search algorithm is O(n) as it iterates over each element of the array in the worst case. The space complexity of the algorithm is O(1) as it only uses a constant amount of extra space to store the index variable.

## Binary Search
The binarySearch() function takes 4 arguments: the sorted list, the lower index of the sublist to search, the upper index of the sublist to search, and the target value. Initially, the lower index is set to 0, and the upper index is set to the length of the list minus 1.

Inside the binarySearch() function, the middle index is calculated as the average of the lower and upper indices, rounded down to the nearest integer using the floor division operator //. If the middle element is equal to the target, then its index is returned. If the target is less than the middle element, the upper bound is set to the index of the middle element minus 1, and the binary search is recursively called on the lower half of the sublist. Otherwise, the lower bound is set to the index of the middle element plus 1, and the binary search is recursively called on the upper half of the sublist.

If the target value is not found within the sublist, the function prints "Not in list".

Finally, outside of the function, the binarySearch() function is called with the given arguments, and the resulting index is printed if the target value is found within the sublist.