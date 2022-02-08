#Link:https://leetcode.com/problems/car-fleet/
#Time and Space Complexity - O(nlogn) and 0(n)

#Logic: we are given position and speed for each car and need to check no of car fleets reaching destination if any car reaches destination earlier than the first
#car then it will become part of the car fleet and can be considered as 1. We will check the time for each car based on position and speed to reach a destination

def carfleet(target,pos:list[int],speed:list[int]):
    pair=[[p,s] for p,s in zip(pos,speed)]
    stack=[]
    for p,s in sorted(pair)[::-1]:
        stack.append((target-p/s))
        if len(stack)>=2 and stack[-1]<=stack[-2]:
            stack.pop()
    return len(stack)