class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            if i == 0:
                point = nums[0]
                answer.append(point)
            else:
                sum_list = nums[:i+1]
                point = sum(sum_list)
                answer.append(point)
        return answer
