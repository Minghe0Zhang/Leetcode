ass Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.res = []
        def dfs(num,hour,minute,idx):
            if(hour>=12 or minute>=60):     return
            if(num==0):
                self.res.append(str(hour) + ":" + "0"*(minute<10) + str(minute))
                return
            for i in range(idx+1,11):
                '''
                if i<= 4: 
                    hour = hour + 2**(i-1)
                else:
                    minute = minute + 2**(i-5)
                '''
                dfs(num-1,int(hour+2**(i-1)*(i<=4)),int(minute+2**(i-5)*(i>4)),i)
        dfs(num,0,0,0)
        return self.res
            
        
