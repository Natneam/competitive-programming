class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        max_index = 0
        #find the maximum
        for i in range(0, len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i
        
        if max_index == 0 or max_index == len(arr) - 1:
            return False
        
        #check the increasing part of the array
        for i in range(1, max_index+1):
            if arr[i-1] >= arr[i]:
                return False
            
        #check the decreasing part of the array
        for i in range(max_index+1, len(arr)):
            if arr[i-1] <= arr[i]:
                return False
        return True