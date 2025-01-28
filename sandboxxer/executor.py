import ast
from .config import ALLOWED_NODES, SAFE_BUILTINS

class CodeExecutor:
    def __init__(self):
        # Define a safe execution environment with limited built-ins
        self.safe_builtins = SAFE_BUILTINS
        # Shared namespace for variables across executions
        self.namespace = {}

    def _validate_code(self, code):
        """Validate the code by parsing it into an AST and checking for unsafe operations."""
        try:
            tree = ast.parse(code, mode='exec')
            self._visit_ast(tree)
        except Exception as e:
            raise ValueError(f"Code validation failed: {e}")

    def _visit_ast(self, node):
        """Visit AST nodes to check for unsafe operations."""
        if type(node) not in ALLOWED_NODES:
            raise ValueError(f"Operation not allowed: {type(node).__name__}")
        for child in ast.iter_child_nodes(node):
            self._visit_ast(child)

    def execute(self, code):
        """Execute the code in a restricted environment with a shared namespace."""
        try:
            self._validate_code(code)
            exec(code, {'__builtins__': self.safe_builtins}, self.namespace)
        except Exception as e:
            if hasattr(e, 'lineno'):
                line_number = e.lineno
                lines = code.splitlines()
                affected_line = lines[line_number - 1] if line_number <= len(lines) else "Unknown line"
                raise RuntimeError(f"Error at line {line_number}: {e}\nAffected line: {affected_line}")
            else:
                raise RuntimeError(f"Error: {e}")