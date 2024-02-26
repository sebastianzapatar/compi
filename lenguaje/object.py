from abc import(
    ABC,
    abstractmethod
)
from enum import(
    auto,
    Enum
)
"""
Se crean los objetos que va a utilizar nuestro interprete
Pueden agregar los tipos de datos que quieran
"""
class ObjecType(Enum):
    BOOLEAN = auto()
    INTEGER = auto()
    NULL = auto()
    STRING = auto()

class Object(ABC):#ABC indica que es una clase abstracta

    @abstractmethod
    def type(self)->ObjecType:
        #Se coloca pass ya que en python es obligatorio colocar algo en los métodos
        #Al ser un método abstracto no se define
        pass
    @abstractmethod
    def inspect(self)->str:
        pass

class Integer(Object):
    def __init__(self,value:int) -> None:
        self.value=value
    def type(self) -> ObjecType:
        return ObjecType.INTEGER
    def inspect(self) -> str:
        return str(self.value)
    
class Boolean(Object):
    def __init__(self,value:bool) -> None:
        self.value=value
    def type(self) -> ObjecType:
        return ObjecType.BOOLEAN
    def inspect(self) -> str:
        return str(self.value)
class Null(Object):
    def type(self) -> ObjecType:
        return ObjecType.NULL
    def inspect(self) -> str:
        return 'empty and cold like her hearth'
class String(Object):
    def __init__(self,value:str) -> None:
        self.value=value
    def type(self) -> ObjecType:
        return ObjecType.STRING
    def inspect(self) -> str:
        return str(self.value)