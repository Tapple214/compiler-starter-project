from components.lexica import MyLexer
from components.memory import Memory
from sly import Parser

# TODO: remove after completion
# class MyParser(Parser):
#     debugfile = 'parser.out'
#     start = 'statement'
#     # Get the token list from the lexer (required)
#     tokens = MyLexer.tokens
#     precedence = (
#         ('left', "+", MINUS),
#         ('left', TIMES, DIVIDE),
#         ('right', UMINUS),
#         )

#     def __init__(self):
#         self.memory:Memory = Memory()

#     @_('NAME ASSIGN expr')
#     def statement(self, p):
#         var_name = p.NAME
#         value = p.expr
#         self.memory.set(variable_name=var_name,value=value, data_type=type(value))
#         # Note that I did not return anything

#     @_('expr')
#     # S -> E
#     def statement(self, p) -> int:
#         return p.expr

#     # The example with literals
#     @_('expr "+" expr')
#     # E -> E + E
#     def expr(self, p):
#         # You can refer to the token 2 ways
#         # Way1: using array
#         print(p[0], p[1], p[2])
#         # Way2: using symbol name. 
#         # Here, if you have more than one symbols with the same name
#         # You have to indiciate the number at the end.
#         return p.expr0 + p.expr1

#     # The example with normal token
#     @_('expr MINUS expr')
#     def expr(self, p):
#         print(p[0], p[1], p[2])
#         return p.expr0 - p.expr1

#     @_('expr TIMES expr')
#     def expr(self, p):
#         return p.expr0 * p.expr1

#     @_('expr DIVIDE expr')
#     def expr(self, p):
#         return p.expr0 / p.expr1

#     # https://sly.readthedocs.io/en/latest/sly.html#dealing-with-ambiguous-grammars
#     # `%prec UMINUS` is the way to override the `precedence` of MINUS to UMINUS.
#     @_('MINUS expr %prec UMINUS')
#     def expr(self, p):
#         return -p.expr

#     @_('LPAREN expr RPAREN')
#     def expr(self, p):
#         return p.expr

#     @_('NUMBER')
#     def expr(self, p):
#         return int(p.NUMBER)


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
    def statement(self, p) -> bool:
        return p.expr

    # Grammar Rule - AND
    @_('expr AND expr')
    def expr(self, p):
        return p.expr0 and p.expr1

    # Grammar Rule - OR
    @_('expr OR expr')
    def expr(self, p):
        return p.expr0 or p.expr1

    # base case - TRUE
    @_('TRUE')
    def expr(self, p) -> bool:
        return True

    # base case - FALSE
    @_('FALSE')
    def expr(self, p) -> bool:
        return False
        
if __name__ == "__main__":
    lexer = MyLexer()
    # parser = MyParser()
    text = "t ∨ f ∧ t" # change to match
    memory = Memory()
    parser = ASTParser()
    result = parser.parse(lexer.tokenize(text))
    print(result)
    # print(memory)