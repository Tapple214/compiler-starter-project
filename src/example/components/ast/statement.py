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

class Expression(ABC): 
    @abstractmethod
    def __init__(self) -> None:
        self.signature:str = ""
        self.value:int = None
        pass

    @abstractmethod
    def run(self) -> None:
        pass

class Expression_logic(Expression):
    def __init__(self, operation:Operations, parameter1:Expression, parameter2:Expression):
        # Init attribute - storing operation and params
        self.operation:Operations = operation       
        self.parameter1:Expression = parameter1
        self.parameter2:Expression = parameter2
        self.value:bool = None
        # Checking Logic
        assert operation in Operations

        # Create a children
        self.children = [self.parameter1, self.parameter2]
        
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
        
        # Prefix output
        self.signature = (
            f"Expression: "
            f"{self.operation.name} "
            f"{self.parameter1.value} "
            f"{self.parameter2.value}"
        )

        print(self)

    def __repr__(self) -> str:
        return self.signature

class Expression_bool(Expression):
    def __init__(self, value: bool) -> None:
        self.value:bool = value
        self.signature:str= str(value)
        
    def run(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return f"Expression_bool:{self.signature}"

if __name__ == "__main__":
    bool1 = Expression_bool(True) # Create True obj
    bool2 = Expression_bool(False) # Create False obj
    # TODO: change expression logic
    expr = Expression_math(Operations.MINUS, parameter1=number1, parameter2=number2)
    expr.run()
    print(expr.value)