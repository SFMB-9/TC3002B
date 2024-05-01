# Rules
```BNF
<assignment> ::= VARIABLE SETTO <expression>
               | VARIABLE SETTO <list>
               | VARIABLE SETTO <flow>

<flow> ::= VARIABLE CONNECT <flow_functions>

<flow_functions> ::= <flow_function_call> CONNECT <flow_functions>
                   | <flow_function_call>

<flow_function_call> ::= VARIABLE LPAREN <params> RPAREN

<factor> ::= <function_call>
           | NUMBER
           | VARIABLE
           | LPAREN <expression> RPAREN

<function_call> ::= VARIABLE LPAREN RPAREN
                  | VARIABLE LPAREN <params> RPAREN

<params> ::= <params> COMMA <expression>
           | <expression>

<list> ::= LBRACKET RBRACKET
         | LBRACKET <elements> RBRACKET

<elements> ::= <elements> COMMA <element>
             | <element>

<element> ::= <expression>
            | <list>

<expression> ::= VARIABLE LBRACKET <index> RBRACKET
               | VARIABLE DOT <append>
               | VARIABLE DOT append
               | VARIABLE LBRACKET <index> RBRACKET SETTO <expression>
               | <expression> PLUS <term>
               | <expression> MINUS <term>
               | <term>
               | STRING
               | <expression> EQUALS <expression>
               | <expression> NEQUALS <expression>
               | <expression> LEQUALS <expression>
               | <expression> GEQUALS <expression>
               | <expression> LESS <expression>
               | <expression> GREATER <expression>
               | <expression> AND <expression>
               | <expression> OR <expression>
               | NOT <expression>
               | LPAREN <expression> RPAREN TERNARY <expression> CASE <expression>
               | IF LPAREN <expression> RPAREN CASE <expression>
               | ELIF LPAREN <expression> RPAREN CASE <expression>
               | ELSE CASE <expression>

<append> ::= VARIABLE LPAREN <expression> RPAREN

<term> ::= <term> TIMES <exponent>
         | <term> DIVIDE <exponent>
         | <exponent>

<exponent> ::= <factor> EXP <factor>
             | <factor>
             | LPAREN <expression> RPAREN

<index> ::= NUMBER
          | NUMBER CASE NUMBER

```