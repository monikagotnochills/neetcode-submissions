class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
     ## Brute force can get on on nested loop thing but n^2 approach but time complexity would go fucking high so we go up with stack 
     # We even deal with monotonic decreasing order 
        res = [0] * len(temperatures)
        stack =[]
        

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT , stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res        
