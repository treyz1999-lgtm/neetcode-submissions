class Solution:
    def isValid(self, s: str) -> bool:
        validPair = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack =[]

        for char in s:
            #check if the character is a closing (key)
            if char in validPair:
                #have to consider if the stack is non empty
                if stack and stack[-1] == validPair[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        #if the stack is empty, we have a valid parentheses
        return len(stack) == 0 
