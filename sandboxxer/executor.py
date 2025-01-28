import ast

class CodeExecutor:
    # List of allowed AST nodes (safe operations)
    ALLOWED_NODES = {
    ast.Module,  # Allow the root module node
    ast.Expr,    # Allow expressions
    ast.Assign,  # Allow assignment
    ast.Store,   # Allow storing variables
    ast.Call,    # Allow function calls
    ast.Name,    # Allow variable names
    ast.Load,    # Allow loading variables
    ast.Constant,# Allow constants
    ast.BinOp,   # Allow binary operations
    ast.Add,     # Allow addition
    ast.Sub,     # Allow subtraction
    ast.Mult,    # Allow multiplication
    ast.Div,     # Allow division
    ast.Mod,     # Allow modulo
    ast.Compare, # Allow comparisons
    ast.Eq,      # Allow equality
    ast.NotEq,   # Allow inequality
    ast.Lt,      # Allow less than
    ast.LtE,     # Allow less than or equal
    ast.Gt,      # Allow greater than
    ast.GtE,     # Allow greater than or equal
    ast.And,     # Allow logical and
    ast.Or,      # Allow logical or
    ast.IfExp,   # Allow conditional expressions
    ast.List,    # Allow lists
    ast.Tuple,   # Allow tuples
    ast.Dict,    # Allow dictionaries
    ast.Set,     # Allow sets
    ast.Index,   # Allow indexing
    ast.Slice,   # Allow slicing
    }

    def __init__(self):
        # Define a safe execution environment with limited built-ins
        self.safe_builtins = {
            'print': print,  # Allow the print function
            'range': range,  # Allow the range function
            'len': len,      # Allow the len function
        }
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
        if type(node) not in self.ALLOWED_NODES:
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