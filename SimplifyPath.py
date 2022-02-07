#Link:https://leetcode.com/problems/simplify-path/

#Converting the path into a canonical form.

def simplifypath(path:str):
    stack=[]
    cur=''
    for i in path+'/':
        if i=='/':
            if cur=='..':
                if stack:
                    stack.pop()
            elif cur!='.' and cur!='':
                stack.append(cur)
            cur=''
        else:
            cur+=i
    return '/'+'/'.join(stack)

