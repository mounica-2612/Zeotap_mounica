class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(type: {self.type}, value: {self.value}, left: {self.left}, right: {self.right})"


def create_rule(rule_string):
    """
    Function to parse a rule string and convert it to an AST.
    """
    import re
    tokens = re.findall(r'\w+|[<>=!]+|\(|\)|AND|OR', rule_string)

    def build_ast(tokens):
        stack = []
        operators = {"AND", "OR"}

        while tokens:
            token = tokens.pop(0)

            if token == '(':
                subtree = build_ast(tokens)
                stack.append(subtree)
            elif token == ')':
                break
            elif token in operators:
                operator_node = Node(node_type="operator", value=token)
                operator_node.left = stack.pop()
                operator_node.right = build_ast(tokens)
                stack.append(operator_node)
            else:
                if re.match(r'[<>=!]', token):
                    operator = token
                    left_operand = stack.pop()
                    right_operand = tokens.pop(0)
                    operand_node = Node(node_type="operand", value=f"{left_operand} {operator} {right_operand}")
                    stack.append(operand_node)
                else:
                    stack.append(token)

        return stack[0] if stack else None

    return build_ast(tokens)


def evaluate_rule(ast, data):
    """
    Evaluates the AST against user data and returns True if the rule is satisfied, otherwise False.
    """
    if ast.type == "operand":
        condition = ast.value.split()
        attribute = condition[0]
        operator = condition[1]
        value = int(condition[2]) if condition[2].isdigit() else condition[2].strip("'")

        if attribute not in data:
            raise ValueError(f"Attribute {attribute} missing in data")

        if operator == '>':
            return data[attribute] > value
        elif operator == '<':
            return data[attribute] < value
        elif operator == '=':
            return data[attribute] == value
        elif operator == '>=':
            return data[attribute] >= value
        elif operator == '<=':
            return data[attribute] <= value
        elif operator == '!=':
            return data[attribute] != value
        else:
            raise ValueError(f"Unknown operator {operator}")

    elif ast.type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)

    return False
