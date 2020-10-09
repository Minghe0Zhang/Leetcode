# 42 接雨水

解法1：
> 1. 找出最高点
> 2. 分别从两边往最高点遍历：记录当前次高点高度，如果下一个数比当前数小，说明可以接到水，在这个格子里接水深度为高度差；
> 如果下一个数比当前次高点大，则更新次高点，此格没有水


解法2：单调栈
维护一个单调栈：即从栈底到栈顶元素逐渐减小。

在遍历墙的过程中：

>   1. 墙的高度小于或等于栈顶元素：入栈，此时不会产生积水
> 2. 墙的高度大于栈顶元素：栈顶元素出栈，此时栈顶元素处会产生积水，产生积水的面积为：（该位置左右墙体的最小高度 - 栈顶元素高度）* 左右墙体距离差

 (第一次接触单调栈，需要再反复体会一下)