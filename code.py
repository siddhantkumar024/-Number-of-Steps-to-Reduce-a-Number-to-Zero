class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        if num==0:
            return 0
        for i in range(num):
            if num%2==0:
                num=num//2
                c+=1
            else:
                num=num-1
                c+=1
            if num==0:
                return c
        
