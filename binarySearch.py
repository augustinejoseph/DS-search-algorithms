def binarySearch(list1, lower, upper, target):
    if lower <= upper:
        middle = (lower+upper) // 2
        if list1[middle] == target:
            return middle
        elif target < list1[middle]:
            upper = middle-1
            return binarySearch(list1, lower, upper, target)
        else:
            lower = middle+1
            return binarySearch(list1, lower, upper, target)
        
    else:
        print("Not in list")
        
list1 = [1,2,3,4,5,6,7,8,9]
target = 8
lower = 0
upper = len(list1)-1
res = binarySearch(list1, lower, upper, target)
if res is not None:
    print(f"Found {list1[res]} at index {res}")
