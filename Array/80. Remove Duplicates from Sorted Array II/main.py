"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice 
and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 
respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified 
to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array 
will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length  = len(nums)
        if length<=2:
            return length
        left, right = 0,1
        count       = 1
        flag_two    = False
        while(right < length):
            if(nums[left]!=nums[right]):
                if flag_two == False:
                    nums[left+1] = nums[right]
                    left, right = left+1, right+1
                    count += 1
                else:
                    left += 1
                    nums[left] = nums[right]
                    right += 1
                    count += 1
                    flag_two = False
            else:
                if not flag_two:
                    flag_two = True
                    nums[left+1] = nums[right]
                    left, right = left+1, right+1
                    count += 1
                else:
                    right += 1
        return count
            



 
if __name__ == "__main__":
    test1  =  [1,1,1,2,2,3]
    test2  = [0,0,1,1,1,1,2,3,3]
    sol = Solution()
    res = sol.removeDuplicates(test1)
    for i in range(res):
        print(test1[i]) 