class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (right +left)//2 #get the mid point
            #check if mid == target
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target: #target is to the right of the mid
                left = mid + 1
            else: #target is to the left of the mid
                right = mid -1
        return -1