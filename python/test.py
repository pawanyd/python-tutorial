import math
class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        middle = math.floor(len(nums) / 2)

        left = self.sortArray(nums[0:middle])
        right = self.sortArray(nums[middle:])

        return self.mergeArray(left , right)

    def mergeArray(self , left , right):
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            elif left[i] >= right[j]:
                res.append(right[j])
                j += 1

        return [*res , *left[i:] , *right[j:]]
    
    
    def majorityElement(self, nums):
        map = {}
        for item in nums:
            if item not in map:
                map[item] = 1
            else:
                map[item] += 1

        majoritycount = math.floor(len(nums) / 2)

        for key , value in enumerate(map):
            if value >= majoritycount:
                return key
            
            
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        letters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        result = []
        def backtrack(path,index):
            if len(digits) == index:
                result.append("".join(path))
                return
            digit = int(digits[index])
            choices = letters.get(digit)
            for i in range(len(choices)):
                path.append(choices[i])
                backtrack(path, index + 1)
                path.pop()


        
        backtrack([],0)
        return result
    
    def twoCitySchedCost(self,costs):

        print(costs)

        costs.sort()

        print(costs)

        return costs
    
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n - 2)
        return self.memo[n]

    
sol = Solution()
# sol.sortArray([5,1,1,2,0,0])
# sol.letterCombinations("23")
sol.climbStairs(4)


        
        