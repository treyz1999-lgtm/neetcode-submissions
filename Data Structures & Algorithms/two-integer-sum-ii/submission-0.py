class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left, right = 0, len(numbers) -1
        if not numbers:
            return res
        while left < right:
            lrSum = numbers[left] + numbers[right]
            if lrSum == target:
                res.append(left + 1)
                res.append(right + 1)
                return res
            elif lrSum > target:
                right -=1
            else:
                left +=1
        return res
            