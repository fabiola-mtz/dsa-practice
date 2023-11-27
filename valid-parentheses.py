"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid. An input string is valid if:
        1.- Open brackets must be closed by the same type of brackets.
        2.- Open brackets must be closed in the correct order.
        3.- Every close bracket has a corresponding open bracket of the same type.
"""

from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        types = {'(':')', '[':']', '{':'}'}
        stack = LifoQueue(maxsize = len(s))

        # Push into stack the values until closing brackets
        for bracket in s:
            if bracket in types.keys():   #1
                stack.put(bracket)
            elif stack.empty() or types[stack.get()] != bracket: # 2
                return False
        
        return stack.empty() == True # 3