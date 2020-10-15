"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is 
transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, 
then A is an indirect friend of C. And we defined a friend circle is a group of students who are 
direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, 
then the ith and jth students are direct friends with each other, otherwise not. And you have to output 
the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
 

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
"""
class Solution(object):
    # def dfs(self,M,i,visited):
    #     if i in visited:
    #         return
    #     else:
    #         visited.append(i)
    #         for j in range(len(M)):
    #             if M[i][j] == 1 and i!=j:
    #                 self.dfs(M,j,visited)
    #                 visited.append(j)

        
    # def findCircleNum(self, M):
    #     """
    #     :type M: List[List[int]]
    #     :rtype: int
    #     """
    #     visited = []
    #     n = len(M)
    #     cirCount = 0
    #     for i in range(n):
    #         if i in visited:
    #             continue
    #         self.dfs(M,i,visited)
    #         cirCount+=1
    #     return cirCount


    def find(self, root,i):
        while(root[i]!=i):
            i = root[i]
        return i

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        root = [i for i in range(n)]
        count = n
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j]==1:
                    par_i = self.find(root,i)
                    par_j = self.find(root,j)
                    if par_i!=par_j:
                        root[par_j] = par_i
                        count-=1
        return count

            

  
        
if __name__ == "__main__":
    M = [[1,1,0],
        [1,1,0],
        [0,0,1]]
    sol = Solution()
    res = sol.findCircleNum(M)
    print(res) #2
    

    