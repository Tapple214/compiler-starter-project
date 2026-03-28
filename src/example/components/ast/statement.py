from enum import Enum
from abc import ABC, abstractmethod

class Statement:
    """What is statement?
    In this calculator project, a statement is each line of math expression.
    In this case, it will consit of tree of math expression
    """
    def __init__(self) -> None:
        root_node
        
# Unique identifiers
class Operations(Enum):
    AND = 0
    OR = 1

# base class
class Expression(ABC): 
    def __init__(self) -> None:
        self.signature: str = ""
        self.value: bool = None

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def tree_str(self, prefix="") -> str:
        pass
    
    # Prefix notation/expression structure (tree)
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

    # Binary node
    def prefix(self):
        return (
            f"{self.operation.name} "
            f"{self.parameter1.prefix()} "
            f"{self.parameter2.prefix()}"
        )

    def tree_str(self, prefix="") -> str:
            lines = []
            lines.append(f"{prefix}{self.operation.name}")  # Current node
            
            # Determine prefix for children
            child_prefix = prefix + "│  "
            
            # Left child (use ├─)
            lines.append(self.parameter1.tree_str(prefix + "├─"))
            # Right child (use └─)
            lines.append(self.parameter2.tree_str(prefix + "└─"))
            
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
        return str(self.value)

    def tree_str(self, prefix="") -> str:
        return f"{prefix}{self.value}"
        
    def run(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return f"Expression_bool:{self.signature}"

if __name__ == "__main__":
    bool1 = Expression_bool(True) # Create True obj
    bool2 = Expression_bool(False) # Create False obj
    expr = Expression_logic(Operations.AND, bool1, bool2)
    expr.run()
    print("Result:", expr.value)
    print("AST Tree:", expr.prefix())
    print(expr.value)