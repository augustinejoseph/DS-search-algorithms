# Time Complexity  : O(n)
# Space Complexity : O(1)

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
        
    return False
    
arr = [1,2,3,4,5,6,7,8,9]
target = 4

index = linearSearch(arr, target)
print(index)

