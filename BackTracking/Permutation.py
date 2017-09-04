ass Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(nums,temp):
            if len(temp)==len(nums):
                self.res.append(temp[:]) #deep copy
            for i in range(len(nums)):
                if nums[i] not in temp:
                        
                    temp.append(nums[i])
                    dfs(nums,temp)
                    temp.pop()
        
        dfs(nums,[])
        return self.res
                        
        
