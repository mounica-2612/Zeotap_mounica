from rule_engine import create_rule, evaluate_rule, Node

def combine_rules(rule_list):
    """
    Combines multiple rules into a single AST using the AND operator by default.
    """
    combined_rule = None

    for rule in rule_list:
        rule_ast = create_rule(rule)

        if combined_rule is None:
            combined_rule = rule_ast
        else:
            combined_rule = Node(node_type="operator", value="AND", left=combined_rule, right=rule_ast)

    return combined_rule


rule1 = ("((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) "
         "AND (salary > 50000 OR experience > 5)")
rule2 = ("((age > 30 AND department = 'Marketing'))"
         " AND (salary > 20000 OR experience > 5)")


combined_ast = combine_rules([rule1, rule2])


def print_ast(node, level=0):
    indent = "  " * level
    if node is not None:
        print(f"{indent}Node(type: {node.type}, value: {node.value})")
        if node.left:
            print(f"{indent}  Left:")
            print_ast(node.left, level + 1)
        if node.right:
            print(f"{indent}  Right:")
            print_ast(node.right, level + 1)


print("Combined AST:")
print_ast(combined_ast)

user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

try:
    result = evaluate_rule(combined_ast, user_data)
    print("Rule Evaluation Result:", result)
except ValueError as e:
    print(f"Error in rule evaluation: {e}")

