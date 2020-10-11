# 80. Remove Duplicates from Sorted Array II

还是快慢指针的思想


更简单的思路：
> 题目要求使用 O(1) 空间复杂度，即不能使用额外空间，思路就是双指针+替换了。

> 指针 i 指向数组头部，题目要求最多只能出现两个重复数字，且数组有序，因此 nums[i] == nums[i + 2] 非法
此时要删除 nums[i + 2] 就要向后找到一个 nums[j]（满足 nums[j] != nums[i]）替换 nums[i + 2] 