# 287. Find the Duplicate Number
Approach 3: Floyd's Tortoise and Hare (Cycle Detection)

check this: https://leetcode.com/problems/find-the-duplicate-number/solution/

使用快慢指针。

将数组看成链表，val 是结点值也是下个节点的地址。因此这个问题就可以转换成判断链表有环，且找出入口节点。

如果有环：快慢指针在某一点相遇
此时再把其中一个指针移到起点，另一个指针移到相遇点（开始绕环跑），那么两个指针必然会在入口相遇