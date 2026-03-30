from components.lexica import MyLexer
from components.memory import Memory
from sly import Parser
from components.ast.statement import Expression, Expression_logic, Expression_bool, Operations

class ASTParser(Parser):
    debugfile = 'parser.out'
    start = 'statement'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    precedence = (
        ('left', OR),
        ('left', AND), # higher priority
        )

    @_('expr')
    def statement(self, p) -> Expression:
        return p.expr

    # Grammar Rule - AND
    @_('expr AND expr')
    def expr(self, p):
        return Expression_logic(Operations.AND, p.expr0, p.expr1)

    # Grammar Rule - OR
    @_('expr OR expr')
    def expr(self, p):
        return Expression_logic(Operations.OR, p.expr0, p.expr1)

    # base case - TRUE
    @_('TRUE')
    def expr(self, p) -> Expression_bool:
        return Expression_bool(True)

    # base case - FALSE
    @_('FALSE')
    def expr(self, p) -> Expression_bool:
        return Expression_bool(False)
        
if __name__ == "__main__":
    lexer = MyLexer()
    text = "t ∨ f ∧ t"
    memory = Memory()
    parser = ASTParser()
    result = parser.parse(lexer.tokenize(text))
    
    print(result)
    print(memory)