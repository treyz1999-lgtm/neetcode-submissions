class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {} # key: number, value: index

        #iterate through the list and check if the remaining value (target - nums[i]) is in our map

        for i in range(len(nums)):
            
            remaining = target - nums[i]

            if remaining in index:
                return [index.get(remaining), i]
            
            if not nums[i] in index: #add it to the dictionary if it is not in there already
                index[nums[i]] = i 

        return []