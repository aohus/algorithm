"""
link : https://leetcode.com/problems/valid-parentheses/
"""


def valid_parentheses(s):
    stack = []
    pair = {"(": ")", "{": "}", "[": "]"}
    for e in s:
        if e in ["(", "{", "["]:
            stack.append(e)
        else:
            if stack.pop() != pair[e]:
                return False

        # if len(stack) == 0:
        #     return True
        # else:
        #     return False
        return True if len(stack) == 0 else False


# 다른 코드
def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "[":
            stack.append("]")
        elif p == "{":
            stack.append("}")
        elif not stack or stack.pop() != p:
            return False
    # return not stack 으로 쓰면 1줄로 줄일 수 있음
    return not stack


print(valid_parentheses("{({[]})}[]()"))
