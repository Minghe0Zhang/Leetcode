"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and 
returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
"""
class Solution:
    def removeDuplicates(self, nums):
        len_uniq = 1
        a        = 0
        while(a < len(nums)-1):
            if(nums[a]!=nums[a+1]):
                len_uniq += 1
                a += 1
            else:
                del nums[a+1]

        print(nums)
        return len_uniq

    def removeDuplicates2(self, nums):
        """
        Method 2 do not need to change length of the array
        """
        if len(nums) == 0:
            return 0
        i,j = 0,1
        num_uniq = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j +=1
            else:
                num_uniq += 1
                i += 1
                nums[i] = nums[j]
                j += 1

        print(nums)
        return num_uniq

        




if __name__ == "__main__":
    test = [1,1,2]
    sol = Solution()
    res = sol.removeDuplicates2(test)
    print(res)