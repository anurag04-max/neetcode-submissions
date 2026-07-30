class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            if len(stack) == 0:
                stack.append(x)
            elif (x < 0 and stack[-1] > 0):
                    if abs(x) == abs(stack[-1]) :
                        stack.pop()
                        continue
                    elif abs(x) <  abs(stack[-1]):
                        continue
                    else:
                        f = False
                        b = False
                        while len(stack) > 0  and stack[-1] > 0:
                            if abs(x) <  abs(stack[-1]):
                                break
                            elif abs(x) == abs(stack[-1]):
                                f = True
                                stack.pop()
                                break
                            elif abs(x) > abs(stack[-1]):
                                b = True
                                stack.pop()
                            if len(stack) > 0:
                                b = False
                        if (len(stack) == 0 and b == True) or (len(stack) > 0  and stack[-1] < 0):
                            stack.append(x)            
            else:
                stack.append(x)    
        ans = []
        while stack:
            ans.append(stack.pop())
        l = 0
        r = len(ans) -1
        while(l <= r):
            ans[l],ans[r] =ans[r],ans[l] 
            l+=1
            r-=1   
        return ans     
                                    