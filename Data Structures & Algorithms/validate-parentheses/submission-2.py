class Solution:
    def isValid(self, s: str) -> bool:
        open_brackt={'(':')','[':']','{':'}'}
        colsed_brackt={')':'(',']':'[','}':'{'}
        stack=[]
        if len(s)%2!=0:
            return False
        for c in s:
            if open_brackt.get(c):
                stack.append(c)
            else:
                if stack and stack[-1]==colsed_brackt[c]:
                    stack.remove(colsed_brackt[c])
                else:
                    return False
        return len(stack)==0
        