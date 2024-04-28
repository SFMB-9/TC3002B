import ply.lex as lex
import ply.yacc as yacc
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
from library import *
# ---------- Graph variables --------------------------
parseGraph = None
draw = True
NODE_COUNTER = 0

#---------- Description -------------------------------
# This program is a simple lexer that can handle
# basic arithmetic operations and variable assignment.
# It also has a symbol table to store the values of
# the variables.

#---------- List of tokens ----------------------------

tokens =(
    'NUMBER',
    "VARIABLE",
    "SETTO", # Assignment
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "EXP",
    "LPAREN", # Left Parentheses
    "RPAREN", # Right Parentheses
    "COMMA",
    "STRING",
    "CONNECT",
    "EQUALS",
    "NEQUALS", # Not equals
    "LEQUALS", # Less or equals
    "GEQUALS", # Greater or equals
    "LESS", # Less than
    "GREATER", # Greater than
    "AND",
    "OR",
    "NOT",
    "TERNARY",
    "CASE",
    "IF",
    "ELIF",
    "ELSE",
    "LBRACKET", # LISTS
    "RBRACKET", # LISTS
    "DOT" # LISTS
)

#---------- Regular expressions -----------------------

t_PLUS = r'\+'
t_SETTO = r'='
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXP = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_CONNECT = r'\->'

t_EQUALS = r'=='
t_NEQUALS = r'!='
t_LEQUALS = r'<='
t_GEQUALS = r'>='
t_LESS = r'<'
t_GREATER = r'>'

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_TERNARY = r'\?'
t_CASE = r':'

t_IF = r'if'
t_ELIF = r'elif'
t_ELSE = r'else'

t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOT = r'\.'
#---------- Symbol table ------------------------------
symbol_table = dict()

# ---------- Predefined functions ----------------------
def printP():
    print("Hello, World!")

def printP2(num):
    print("Hello, World! " + str(num))

#---------- node functions -----------------------------
def add_node(attr):
    global parseGraph # Parse Graph is a global variable that is used to store the nodes and edges of the parse tree, it is a networkx graph.
    global NODE_COUNTER # Node counter is a global variable that is used to assign a unique identifier to each node in the parse tree.
    attr["counter"] = NODE_COUNTER # Assign the current value of the node counter to the node.
    parseGraph.add_node(NODE_COUNTER, **attr) # Add the node to the parse graph.
    NODE_COUNTER += 1 # Increment the node counter.

    return parseGraph.nodes[NODE_COUNTER - 1] # Return the node that was just added to the graph.
    

#---------- Dictionary of reserved words --------------
symbol_table["pi"] = 3.14159265359 # Predefined values
symbol_table["e"] = 2.71828182846 # Predefined values
symbol_table["phi"] = 1.61803398875 # Predefined values
symbol_table["tau"] = 6.28318530718 # Predefined values
symbol_table["gamma"] = 0.5772156649 # Predefined values
symbol_table["inf"] = float('inf') # Predefined values
symbol_table["nan"] = float('nan') # Predefined values
symbol_table["true"] = 1 # Predefined values
symbol_table["false"] = 0 # Predefined values
symbol_table["print"] = print # Predefined values
symbol_table["printP"] = printP # Predefined values
symbol_table["printP2"] = printP2 # Predefined values
symbol_table["exit"] = "exit" # Predefined values
symbol_table["symbols"] = "symbols" # Predefined values
symbol_table["max"] = max              # Predefined values


symbol_table["load_image"] = load_image # Predefined values
symbol_table["save_image"] = save_image # Predefined values
symbol_table["show_image"] = show_image # Predefined values
symbol_table["gen_matrix"] = gen_matrix # Predefined values
symbol_table["gen_vector"] = gen_vector # Predefined values


#---------- Ignored characters ------------------------

# Ignored characters are those that are not used in the grammar but are used to separate tokens. 

#---------- Regular expressions as functions ----------

def t_NUMBER(t):
    r'\d+\.?\d*'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*' # Check for valid variable names, they must start with a letter or an underscore and can be followed by letters, numbers or underscores.
    return t

def t_STRING(t):
    r'\".*\"' # Check for valid strings, they must be enclosed in double quotes.
    t.value = t.value[1:-1] # Remove the double quotes from the string.
    return t

#---------- Boilerplate code --------------------------

def t_newline(t):
    r'\n+' # Check for one or more newline characters.
    t.lexer.lineno += len(t.value) # Increment the line number by the number of newline characters.

t_ignore = ' \t' # Ignore spaces and tabs.

def t_error(t):
    print("Error") # Print an error message if an invalid token is found.
    t.lexer.skip(1)

#---------- Building the lexer -----------------------------
    
lexer = lex.lex()

#---------- Parsing rules ----------------------------------
def p_assignment_assign(p):
    '''
    assignment : VARIABLE SETTO expression
               | VARIABLE SETTO list
    '''
    node = add_node({"type":"ASSIGN", "label":"=", "value":""})
    node_variable = add_node({"type":"VARIABLE_ASSIGN", "label":f"VAR_{p[1]}", "value":p[1]})
    parseGraph.add_edge(node["counter"], node_variable["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

# ---------- Assignment flow -----------------------------

def p_assignment_flow(p):
    '''
    assignment : VARIABLE SETTO flow
    '''
    pass

def p_flow_form(p):
    '''
    flow : VARIABLE CONNECT flow_functions
    '''
    pass

def p_flow_functions(p):
    '''
    flow_functions : flow_function_call CONNECT flow_functions
    '''
    pass

def p_flow_function_single(p):
    '''
    flow_functions : flow_function_call
    '''
    pass


def p_flow_function_call(p):
    '''
    flow_function_call : VARIABLE LPAREN params RPAREN
    '''
    pass
    
#---------- Function call ------------------------------
def p_factor_function_call(p):
    '''
    factor : function_call
    '''
    p[0] = p[1]


def p_function_call_no_params(p):
    '''
    function_call : VARIABLE LPAREN RPAREN
    '''
    p[0] = add_node({"type":"FUNCTION_CALL", "label":f"FUN_{p[1]}", "value":p[1]})


def p_function_call_params(p):
    '''
    function_call : VARIABLE LPAREN params RPAREN
    '''
    print(p[3])
    node = add_node({"type":"FUNCTION_CALL", "label":f"FUN_{p[1]}", "value":p[1]})
    for n in p[3]:
        parseGraph.add_edge(node["counter"], n["counter"])
    p[0] = node

def p_params(p):
    '''
    params : params COMMA expression
        | expression
    '''
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

#---------- Lists -----------------------------------------
def p_empty_list(p):
    '''
    list : LBRACKET RBRACKET
    '''
    p[0] = add_node({"type":"EMPTY_LIST", "label":"[]", "value":[]})

def p_list_literal(p):
    '''
    list : LBRACKET elements RBRACKET
    '''
    node = add_node({"type":"LIST", "label":"[]", "value":p[2]})
    for n in p[2]:
        parseGraph.add_edge(node["counter"], n["counter"])
    p[0] = node

def p_elements(p):
    '''
    elements : elements COMMA element
             | element
    '''
    if len(p) > 2:
        p[0] = p[1] + [p[3]] # Add the expression to the list of elements.
    else:
        p[0] = [p[1]] # Create a new list with the expression as the first element.

def p_element(p):
    '''
    element : expression
            | list
    '''
    p[0] = p[1]

def p_list_index(p):
    '''
    expression : expression LBRACKET index RBRACKET
    '''
    node = add_node({"type":"INDEX", "label":"INDEX", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_index(p):
    '''
    index : NUMBER
    '''
    p[0] = add_node({"type":"NUMBER", "label":f"[{p[1]}]", "value":p[1]})

def p_list_append(p):
    '''
    expression : expression DOT append
    '''
    node = add_node({"type":"APPEND", "label":"append", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_append(p):
    '''
    append : VARIABLE LPAREN expression RPAREN
    '''
    p[0] = p[3] # Return the value to be appended to the list.

def p_index_assign(p):
    '''
    expression : expression LBRACKET index RBRACKET SETTO expression
    '''
    node = add_node({"type":"INDEX_ASSIGN", "label":"INDEX_ASSIGN", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    parseGraph.add_edge(node["counter"], p[6]["counter"])
    p[0] = node

#---------- Assignment expression -------------------------
def p_assignment_expression(p):
    ''' 
    assignment : expression
    '''
    p[0] = p[1]
    

#---------- Expression PLUS ------------------------------------
def p_expression_plus(p):
    """
    expression : expression PLUS term
    """
    node = add_node({"type":"PLUS", "label":"+", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

#---------- Expression MINUS -----------------------------------
def p_expression_minus(p):
    """
    expression : expression MINUS term
    """
    node = add_node({"type":"MINUS", "label":"-", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

#---------- Expression Term -------------------------------------
def p_expression_term(p):
    """
    expression : term 
            | string
    """
    p[0] = p[1]

def p_string(p):
    '''
    string : STRING
    '''
    p[0] = add_node({"type":"STRING", "label":f"STR_{p[1]}", "value":p[1]})

#---------- Term Times ------------------------------------------
def p_term_times(p):
    '''
    term : term TIMES exponent
    '''
    node = add_node({"type":"TIMES", "label":"*", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    p[0] = node

#---------- Term Divide ------------------------------------------
def p_term_divide(p):
    '''
    term : term DIVIDE exponent
    '''
    node = add_node({"type":"DIVIDE", "label":"/", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    p[0] = node

def p_term_exponent(p):
    '''
    term : exponent
    '''
    p[0] = p[1]

#---------- Exponent Exponent ---------------------------
def p_exponent_exp(p):
    '''
    exponent : factor EXP factor
    '''
    node = add_node({"type":"POWER", "label":"POW", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    p[0] = node

#---------- Exponent Factor -----------------------------
def p_exponent_factor(p):
    '''
    exponent : factor
    '''
    p[0] = p[1]

#---------- Parentheses ---------------------------------
def p_exponent_parent(p):
    '''
    exponent : LPAREN expression RPAREN
    '''
    node = add_node({"type":"GROUP", "label":"{}", "value":""})
    parseGraph.add_edge(node["counter"], p[2]["counter"])
    p[0] = node

#---------- Factor --------------------------------------
def p_factor_num(p):
    ''' 
    factor : NUMBER
    '''
    p[0] = add_node({"type":"NUMBER", "label":f"NUM_{p[1]}", "value":p[1]})


#---------- Variable assignment -------------------------
def p_factor_id(p):
    ''' 
    factor : VARIABLE
    '''
    p[0] = add_node({"type":"VARIABLE", "label":f"VAR_{p[1]}", "value":p[1]})
    
#---------- Comparison operators ------------------------
def p_expression_equals(p):
    '''
    expression : expression EQUALS expression
    '''
    node = add_node({"type":"EQUALS", "label":"==", "value":""}) # Create a new node for the equals operation.
    parseGraph.add_edge(node["counter"], p[1]["counter"]) # Add an edge from the equals node to the left side of the expression.
    parseGraph.add_edge(node["counter"], p[3]["counter"]) # Add an edge from the equals node to the right side of the expression.
    p[0] = node # Set the result of the operation to the equals node.

def p_expression_nequals(p):
    '''
    expression : expression NEQUALS expression
    '''
    node = add_node({"type":"NEQUALS", "label":"!=", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_lequals(p):
    '''
    expression : expression LEQUALS expression
    '''
    node = add_node({"type":"LEQUALS", "label":"<=", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_gequals(p):
    '''
    expression : expression GEQUALS expression
    '''
    node = add_node({"type":"GEQUALS", "label":">=", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_less(p):
    '''
    expression : expression LESS expression
    '''
    node = add_node({"type":"LESS", "label":"<", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_greater(p):
    '''
    expression : expression GREATER expression
    '''
    node = add_node({"type":"GREATER", "label":">", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

#---------- Logical operators ---------------------------
def p_expression_and(p):
    '''
    expression : expression AND expression
    '''
    node = add_node({"type":"AND", "label":"&&", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_or(p):
    '''
    expression : expression OR expression
    '''
    node = add_node({"type":"OR", "label":"||", "value":""})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_not(p):
    '''
    expression : NOT expression
    '''
    node = add_node({"type":"NOT", "label":"!", "value":""})
    parseGraph.add_edge(node["counter"], p[2]["counter"])
    p[0] = node

#---------- Conditional operators ------------------------
def p_expression_ternary(p):
    '''
    expression : LPAREN expression RPAREN TERNARY expression CASE expression
    '''
    node = add_node({"type": "TERNARY", "label": "?:", "value": ""})
    parseGraph.add_edge(node["counter"], p[2]["counter"])  # Condition
    parseGraph.add_edge(node["counter"], p[5]["counter"])  # True branch
    parseGraph.add_edge(node["counter"], p[7]["counter"])  # False branch
    p[0] = node

def p_expression_if(p):
    '''
    expression : IF LPAREN expression RPAREN CASE expression
    '''
    node = add_node({"type": "IF", "label": "IF", "value": ""})
    parseGraph.add_edge(node["counter"], p[3]["counter"])  # Condition
    parseGraph.add_edge(node["counter"], p[6]["counter"])  # True branch
    p[0] = node

def p_expression_elif(p):
    '''
    expression : ELIF LPAREN expression RPAREN CASE expression
    '''
    node = add_node({"type": "ELIF", "label": "ELIF", "value": ""})
    parseGraph.add_edge(node["counter"], p[3]["counter"])  # Condition
    parseGraph.add_edge(node["counter"], p[6]["counter"])  # True branch
    p[0] = node

def p_expression_else(p):
    '''
    expression : ELSE CASE expression
    '''
    node = add_node({"type": "ELSE", "label": "ELSE", "value": ""})
    parseGraph.add_edge(node["counter"], p[3]["counter"])  # True branch
    p[0] = node

#---------- parse tree ---------------------------------
def exexute_parse_tree(tree):
    root = tree.nodes[0]
    root_id = 0
    res = visit_node(tree, root_id, -1)
    if(type(res)== int or type(res) == float):
        print(f"Result: {res}")

# ---------- Visit node function -------------------------
def visit_node(tree, node_id, from_id):
    children = tree.neighbors(node_id)
    res= []
    for c in children:
        if(c != from_id):
            res.append(visit_node(tree, c, node_id))

    current_node = tree.nodes[node_id]
    print( f"From Node {node_id}", res) # Print the node id and the values of the children nodes.

    # Here we will implement the logic to evaluate the parse tree nodes.

    if current_node["type"] == "ROOT":
        return res[0] # Return the value of the root node.
    
    if current_node["type"] == "ASSIGN":
        symbol_table[res[0]] = res[1] # Assign the value of the right side of the assignment to the variable on the left side.
        return res[1]
    
    if current_node["type"] == "NUMBER":
        return current_node["value"] # Return the value of the number node.
    
    if current_node["type"] == "STRING":
        return current_node["value"] # Return the value of the string node.

    if current_node["type"] == "VARIABLE_ASSIGN":
        return current_node["value"] # Return the value of the variable node.
    
    if current_node["type"] == "PLUS":
        return res[0] + res[1] # Return the sum of the two children nodes.
    
    if current_node["type"] == "VARIABLE":
        return symbol_table[current_node["value"]] # Return the value of the variable from the symbol table.
    
    if current_node["type"] == "MINUS":
        return res[0] - res[1] # Return the difference of the two children nodes.
    
    if current_node["type"] == "TIMES":
        return res[0] * res[1] # Return the product of the two children nodes.
    
    if current_node["type"] == "DIVIDE":
        return res[0] / res[1] # Return the division of the two children nodes.
    
    if current_node["type"] == "POWER":
        return pow(res[0], res[1]) # Return the power of the two children nodes. (res[0] ^ res[1])
    
    if current_node["type"] == "GROUP":
        return res[0] # Return the value of the child node.
    
    if current_node["type"] == "FUNCTION_CALL":
        v = current_node["value"]
        print("**** HERE Function call: ", v, " ****")
        if v in symbol_table:
            fn = symbol_table[v]
            if callable(fn):
                try:
                    res = fn(*res)
                    return res
                except Exception as e:
                    print("Error in function call", e)
                    return "Error"
                
            else:
                print(f"Error function {v}, IS NOT of type function")
                return "Error"
        else:
            fn = search_cv2(v)
            if fn is not None:
                try :
                    res = fn(*res)
                    return res
                
                except Exception as e:
                    print("HERE *** Error in function call", e, v," FN: " ,fn," RES: ", res)
                    return "Error"
                else:
                    print("Error function", v, "not found")
                    return "Error"
            else:
                print("Error function", v, "not found")
                return "Error"
    
    if current_node["type"] == "EQUALS":
        if res[0] == res[1]:
            return symbol_table["true"]
        else:
            return symbol_table["false"]
    
    if current_node["type"] == "NEQUALS":
        if res[0] != res[1]:
            return symbol_table["true"]
        else:
            return symbol_table["false"]
    
    if current_node["type"] == "LEQUALS":
        if res[0] <= res[1]:
            return symbol_table["true"]
        else:
            return symbol_table["false"]
    
    if current_node["type"] == "GEQUALS":
        if res[0] >= res[1]:
            return symbol_table["true"]
        else:
            return symbol_table["false"]
    
    if current_node["type"] == "LESS":
        if res[0] < res[1]:
            return symbol_table["true"]
        else:
            return symbol_table["false"]
        
    if current_node["type"] == "GREATER":
        if res[0] > res[1]:
            return symbol_table["true"]
        else:
            return symbol_table["false"]
        
    if current_node["type"] == "AND":
        if res[0] and res[1]:
            return symbol_table["true"]
        else:
            return symbol_table["false"]
        
    if current_node["type"] == "OR":
        if res[0] or res[1]:
            return symbol_table["true"]
        else:
            return symbol_table["false"]
        
    if current_node["type"] == "NOT":
        if not res[0]:
            return symbol_table["true"]
        else:
            return symbol_table["false"]
        
    if current_node["type"] == "TERNARY":
        if res[0]:
            return res[1]
        else:
            return res[2]
    
    # if current_node["type"] == "IF":
    #     if res[0]:
    #         return res[1]
    #     else:
    #         return "Error"
    #     
    # if current_node["type"] == "ELIF":
    #     if res[0]:
    #         return res[1]
    #     else:
    #         return "Error"
    #     
    # if current_node["type"] == "ELSE":
    #     return res[0]

    if current_node["type"] == "EMPTY_LIST":
        return []
    
    if current_node["type"] == "LIST":
        return res[0:]
    
    if current_node["type"] == "INDEX":
        return res[0][res[1]]
    
    if current_node["type"] == "INDEX_ASSIGN":
        res[0][res[1]] = res[2]
        return res[0]
    if current_node["type"] == "APPEND":
        res[0].append(res[1])
        return res[0]
    
    return "Error"
#---------- Error handling ------------------------------
def p_error(p):
    print("Syntax error on input ", p)


#---------- Building the parser ------------------------
parser = yacc.yacc()
#---------- Testing the lexer -------------------------

while True:
    try:
        data = input("> ")
        if(data == "exit"):
            break
        if(data == "symbols"):
            print(symbol_table)
            continue

        
    except EOFError:
        break
    
    if not data: continue
    NODE_COUNTER = 0 # Reset the node counter.
    parseGraph = nx.Graph() # Create a new graph for the parse tree.
    root = add_node({"type":"ROOT", "label":"ROOT"}) # Add the root node to the parse tree.
    result = parser.parse(data) # Parse the input data.
    parseGraph.add_edge(root["counter"], result["counter"]) # Add an edge from the root node to the result node.
    labels = nx.get_node_attributes(parseGraph, 'label') # Get the labels of the nodes in the parse tree.
    if (draw):
        
        # pos = graphviz_layout(parseGraph, prog="dot")  # commented out if on MacOs (not supported)
        nx.draw(parseGraph,labels=labels, with_labels=True, font_weight='bold') # pos=pos)
        plt.show()

    exexute_parse_tree(parseGraph)


print("Finished, accepted input.")