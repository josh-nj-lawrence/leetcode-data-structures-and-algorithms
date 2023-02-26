class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {"(":")","[":"]","{":"}"} # Keys are opening, values are closing
        for x in s:
            if x in braces.values():
                # Check if last on stack is corresponding close
                try:
                    if stack.pop() != corresponding_open(braces, x):
                        return False
                except IndexError:
                    return False
            else:
                stack.append(x)
        if len(stack) == 0:
            return True
        return False    
    
def corresponding_open(braces,x):
        """
            Provide closing bracket and return corresponding open bracket
        """
        for y,z in braces.items():
            if z == x:
                return y
            
# Results: 33.21% time (39ms) 61.2% space (13.9MB)