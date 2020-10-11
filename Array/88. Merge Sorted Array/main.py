"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        merge_idx = m+n-1
        idx1      = m-1
        idx2      = n-1
        while(merge_idx>=0):
            if idx1 < 0:
                nums1[merge_idx] = nums2[idx2]
                idx2-=1
                merge_idx-=1
            elif idx2<0:
                return
            elif nums1[idx1] <= nums2[idx2]:
                nums1[merge_idx] = nums2[idx2]
                idx2-=1
                merge_idx-=1
            else:
                nums1[merge_idx] = nums1[idx1]
                idx1-=1
                merge_idx-=1
            
        return
        
        
 
if __name__ == "__main__":
    nums1 = [1,4,7,0,0,0] 
    m = 3
    nums2 = [2,5,6]       
    n = 3
    sol = Solution()
    sol.merge(nums1,m,nums2,n)
    for res in nums1:
        print(res) #[1,2,2,3,5,6]