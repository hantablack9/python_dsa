import re


def infix_to_postfix(expression: str) -> str:
    """
    Infix to postfix notation using stacks
    """

    def precedence(sign: str) -> int:
        if sign == "^":
            return 3
        elif sign in {"*", "/"}:
            return 2
        elif sign in {"+", "-"}:
            return 1
        else:
            return -1

    def is_right_associative(op: str) -> bool:
        return op == "^"

    stack = []
    result = []

    tokens = re.findall(r"\d+|\w+|[+*/^()-]", expression.replace(" ", ""))

    for token in tokens:
        if re.match(r"\w+", token):
            result.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()

        else:
            while (
                stack
                and stack[-1] != "("
                and (
                    precedence(token) <= precedence(stack[-1])
                    and not is_right_associative(token)
                )
            ):
                result.append(stack.pop())

            stack.append(token)

    while stack:
        result.append(stack.pop())

    return " ".join(result)


if __name__ == "__main__":
    expr = input("Enter an infix math expression:")
    print(infix_to_postfix(expr))
