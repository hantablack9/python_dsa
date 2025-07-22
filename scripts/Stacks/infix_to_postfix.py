"""
Infix expr: (a+b)*(c-d)/e

Postfix expr: ab+cd-*e/

Reference: https://www.geeksforgeeks.org/dsa/convert-infix-expression-to-postfix-expression/

Order of execution

"""


def infix_to_postfix(expr: str) -> str:
    def precedence(sign: str) -> int:
        if sign == "^":
            return 3
        elif sign in ("/", "*"):
            return 2
        elif sign in ("+", "-"):
            return 1
        else:
            return -1

    stack = []
    result = ""

    for char in expr:
        """
        If the scanned character is alphanumeric, 
        add it to the output string.
        """
        if char.isalnum():
            result = result + char

        # If the scanned character is an '(',
        # push it to the stack.

        elif char == "(":
            stack.append(char)

        # If the scanned character is an ')',
        # pop and add to the output string from the stack
        # until an '(' is encountered.

        elif char == ")":
            while stack and stack[-1] != "(":
                result = result + stack.pop()
            if stack and stack[-1] == "(":
                stack.pop()
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                result = result + stack.pop()
            stack.append(char)

    while stack:
        result = result + stack.pop()

    return result


if __name__ == "__main__":
    expr = input("Enter an infix math expression:")
    print(infix_to_postfix(expr))
