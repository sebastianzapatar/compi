from re import match
from lenguaje.token import(
    Token,
    TokenType,
    lookup_token_type
)
"""
El lexer es le que identifica
cual token es y luego se pasa para generar el arbol
Y ser evaluado
"""
class Lexer:
    """
    Se inilizan las varialbes para utilizar en la clase
    """
    def __init__(self, source:str)->None:
        self._source = source
        self._current_pos = 0
        self._current_char = ""
        self._read_current_pos=0
        self._read_character()
    """
    Se asigna el token y se lee el siguiente caracter
    """
    def _read_character(self)->None:
        if self._read_current_pos >= len(self._source):
           self._current_char=""
        else:
            self._current_char = self._source[self._read_current_pos]
        self._current_pos =self._read_current_pos
        self._read_current_pos +=1
    """
    Para evitar espacios en blanco
    """
    def _skip_whitespace(self)->None:
        while self._current_char.isspace():
            self._read_character() 
    """
    peek_character leer el siguiente caracter 
    sin necesidad de avanzar en el cursor
    """
    def _peek_character(self)->str:
        if self._read_current_pos >= len(self._source):
            return ""
        else:
            return self._source[self._read_current_pos]
    """
    Para verificar que el caracter es una letra, soporta español
    """
    def is_letter(self,character:str)->bool:
        return bool(match(r'^[a-záéíóúA-ZÁÉÍÓÚñÑ_]$',character))
    """
    Para evaluar si es un número
    el d indica si \d significa que es un número
    """
    def is_number(self,character:str)->bool:
        return bool(match(r'^\d$',character))
    """
    Función para leer y devolver identenficadores
    """
    def _read_identifier(self)->str:
        initial_position=self._current_pos
        is_first_letter=True
        while self.is_letter(self._current_char) or \
         (not is_first_letter and self.is_number(self._current_char)):
            self._read_character()
            is_first_letter=False
        return self._source[initial_position:self._current_pos]
    """
    Funcion para retornar si es un número
    """
    def _read_number(self):
        initial_positon=self._current_pos
        while self.is_number(self._current_char):
            self._read_character()
        return self._source[initial_positon:self._current_pos]
    """
    Evalua cada token y devuelve su tipo
    """
    def next_token(self):
        
        self._skip_whitespace()
        if match(r'^=$', self._current_char):
            if self._peek_character() == "=":
                self._read_character()
                token = Token(TokenType.EQ, "==")
            else:
                token = Token(TokenType.ASSIGN, self._current_char)
        elif match(r'^\+$', self._current_char):
            token = Token(TokenType.PLUS, self._current_char)
        elif match(r'^,$', self._current_char):
            token = Token(TokenType.COMMA, self._current_char)
        elif match(r'^;$', self._current_char):
            token = Token(TokenType.SEMICOLON, self._current_char)
        elif match(r'^$', self._current_char):
            token = Token(TokenType.EOF, self._current_char)
        elif match(r'^>$',self._current_char):
            if self._peek_character() == "=":
                self._read_character()
                token = Token(TokenType.GTE, ">=")
            else:
                token = Token(TokenType.GT, self._current_char)
        elif match(r'^<$',self._current_char):
            if self._peek_character() == "=":
                self._read_character()
                token = Token(TokenType.LTE, "<=")
            else:
                token = Token(TokenType.LT, self._current_char)
        elif match(r'^!$',self._current_char):
            if self._peek_character() == "=":
                self._read_character()
                token = Token(TokenType.NOE, "!=")
            else:
                token = Token(TokenType.NOT, self._current_char)
        elif self.is_letter(self._current_char):
            literal=self._read_identifier()
            token_type=lookup_token_type(literal)
            return Token(token_type,literal)
        elif self.is_number(self._current_char):
            literal=self._read_number()
            return Token(TokenType.INT,literal)
        else:
            token = Token(TokenType.ILLEGAL, self._current_char)
        self._read_character()
        return token