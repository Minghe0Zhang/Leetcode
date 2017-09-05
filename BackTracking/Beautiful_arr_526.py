ass Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.count = 0
        def dfs(N,step,temp):
            if step==N+1:
                self.count = self.count+1
                return
            for i in range(1,N+1):
                if i not in temp and (i%step==0 or step%i==0):
                    temp.append(i)
                    dfs(N,step+1,temp)             
                    temp.pop()
            return
                    
        dfs(N,1,[])
        return self.count
            
                    
