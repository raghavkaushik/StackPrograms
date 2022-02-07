#Link:https://leetcode.com/problems/largest-rectangle-in-histogram/

#Complexity- O(n) (Time and Space)


#Logic: we use a stack to store the pair of index and heights and only pop when the next height is smaller than current and find the max area till current.

def rectangle(arr):
    maxarea=0
    stack=[]
    for i, h in enumerate(arr):
        start=i
        while stack and stack[-1][1]>h:
            index,height=stack.pop()
            maxarea=max(height*(i-index),maxarea)
            start=index
        stack.append((start,h))

    for i,h in stack:
        maxarea=max(maxarea,h*(len(arr)-i))
    return maxarea