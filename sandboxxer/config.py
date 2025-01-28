
import ast

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

# Safe built-in functions
SAFE_BUILTINS = {
    'print': print,  # Allow the print function
    'range': range,  # Allow the range function
    'len': len,      # Allow the len function
}