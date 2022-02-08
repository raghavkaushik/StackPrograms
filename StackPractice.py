#Largest Rectangle
import collections


def rectangle(arr):
    maxarea = 0
    stack = []
    for i,h in enumerate(arr):
        start=i
        while stack and stack[-1][1]>h:
            index,height=stack.pop()
            maxarea=max(maxarea,height*(i-index))
            start=index
        stack.append((start,h))
    for i,h in stack:
        maxarea=max(maxarea,h*(len(arr)-i))
    return maxarea

#generate Parentheses
def parentheses(n):
    stack=[]
    res=[]
    def backtrack(open,close):
        if open==close==n:
            res.append(''.join(stack))
            return

        if open<n:
            stack.append('(')
            backtrack(open+1,close)
            stack.pop()

        if close<open:
            stack.append(')')
            backtrack(open,close+1)
            stack.pop()
        backtrack(0,0)
    return res

#design min stack
stack=collections.deque()
minstack=collections.deque()
def push(val):
    stack.append(val)
    minval=min(val,stack[-1] if stack else val)
    minstack.append(minval)
def topview():
    print(stack[-1])
def popval():
    stack.pop()
    minstack.pop()
def getmin():
    print(minstack[-1])

def dailytemp(arr):
    res=[0]*arr
    stack=[]
    for i,t in enumerate(arr):
        while stack and t>stack[-1][1]:
            index,temp=stack.pop()
            res[index]=i-index
        stack.append([i,temp])
    return res

