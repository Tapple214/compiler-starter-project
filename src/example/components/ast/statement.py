from enum import Enum
from abc import ABC, abstractmethod

class Statement:
    """What is statement?
    In this calculator project, a statement is each line of expression.
    In this case, it will consist of tree of expression
    """
    def __init__(self) -> None:
        root_node
        
# Unique identifiers
class Operations(Enum):
    AND = "∧"
    OR = "∨"

# base class
class Expression(ABC): 
    def __init__(self) -> None:
        self.signature: str = ""
        self.value: bool = None

    @abstractmethod
    def run(self) -> None:
        pass

    # Tree structure
    @abstractmethod
    def tree_str(self, prefix="") -> str:
        pass
    
    # Prefix notation/expression structure 
    @abstractmethod
    def prefix(self):
        pass

class Expression_logic(Expression):
    
    def __init__(self, operation:Operations, parameter1:Expression, parameter2:Expression):
        super().__init__() # Runs the base class's constructor (__init__)

        # Init attribute - storing operation and params
        self.operation:Operations = operation       
        self.parameter1:Expression = parameter1
        self.parameter2:Expression = parameter2
        self.value:bool = None
        # Checking Logic
        assert operation in Operations

        # Create a children
        self.children = [self.parameter1, self.parameter2]

    # Binary node - Prefix notation/expression
    def prefix(self):
        """Return prefix notation of expression"""
        return (
            f"{self.operation.name} "
            f"{self.parameter1.prefix()} "
            f"{self.parameter2.prefix()}"
        )


    def tree_str(self, prefix="", is_last=True) -> str:
        """Return tree as string with ├─ and └─."""
        lines = []
        connector = "└─" if is_last else "├─"
        lines.append(f"{prefix}{connector}{self.operation.name}")

        # Prepare prefix for children
        if is_last:
            child_prefix = prefix + "   "  # No vertical line, last child
        else:
            child_prefix = prefix + "│  "  # Show vertical line for siblings

        # Left child is never the last if right child exists
        lines.append(self.parameter1.tree_str(child_prefix, is_last=False))
        lines.append(self.parameter2.tree_str(child_prefix, is_last=True))

        return "\n".join(lines)
        
    def run(self) -> None:
        # evaluate child first
        for child in self.children:
            child.run()
            print(child)

        if(self.operation == Operations.AND):
            self.value = self.parameter1.value and self.parameter2.value
        elif(self.operation == Operations.OR):
            self.value = self.parameter1.value or self.parameter2.value
        else:
            raise ValueError(f"{self.operation=} is not supported.")
        
        # Final result (Prefix format)
        self.signature = f"{self.operation.name} {self.parameter1.value} {self.parameter2.value}"
        print(self)

    def __repr__(self) -> str:
        return self.signature

class Expression_bool(Expression):
    def __init__(self, value: bool) -> None:
        self.value:bool = value
        self.signature:str= str(value)

    # Leaf node
    def prefix(self):
        return "t" if self.value else "f"

    def tree_str(self, prefix="", is_last=True) -> str:
        connector = "└─" if is_last else "├─"
        return f"{prefix}{connector}{'t' if self.value else 'f'}"
        
    def run(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return f"Expression_bool:{self.prefix()}"

if __name__ == "__main__":
    bool1 = Expression_bool(True) # Create True obj
    bool2 = Expression_bool(False) # Create False obj
    expr = Expression_logic(Operations.AND, bool1, bool2)
    expr.run()
    print("Result:", expr.value)
    print("AST Tree:", expr.prefix())
    print(expr.value)