from abc import(
    ABC,
    abstractmethod
)
from typing import(
    List,
    Optional
)
from lenguaje.token import Token



class ASTNode(ABC):
    @abstractmethod
    def token_literal(self)->str:
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass
class Statment(ASTNode):
    def __init__(self,token:Token) -> None:
        self.token=token
    def token_literal(self) -> str:
        return self.token.literal
class Expression(ASTNode):
    def __init__(self,token:Token) -> None:
        self.token=token
    def token_literal(self) -> str:
        return self.token.literal
class Program(ASTNode):
    def __init__(self,statements:List[Statment]) -> None:
        self.statements=statements
    def token_literal(self) -> str:
        if len(self.statements)>0:
            return self.statements[0].token_literal()
        return ''
    """
    Se crea un string con la lista de todos los staments
    """
    def __str__(self) -> str:
        out:List[str]=[]
        for statement in self.statements:
            out.append(str(statement))
        #.join vuelve una lista en un string
        return ''.join(out)
class Identifier(Expression):
    def __init__(self, token: Token,value:str) -> None:
        super().__init__(token)
        self.value=value
    def __str__(self) -> str:
        return self.value

class LetStatement(Statment):
    def __init__(self, token: Token,
                 name:Optional[Identifier],
                 value:Optional[Expression]=None) -> None:
        super().__init__(token)
        self.name=name
        self.value=value
    def __str__(self) -> str:
        return f'{self.token_literal()}{str(self.name)}={str(self.value)}'

class ReturnStatement(Statment):
    def __init__(self, token: Token,
                 return_value:Optional[Expression]) -> None:
        super().__init__(token)
        self.return_value=return_value
    def __str__(self) -> str:
        return f'{self.token_literal()}{str(self.return_value)}'
    
class ExpressionStatement(Statment):
    def __init__(self, token: Token,
                 expression:Optional[Expression]) -> None:
        super().__init__(token)
        self.expression=expression
    
    def __str__(self) -> str:
        return str(self.expression)