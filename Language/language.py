with open("code.txt") as t:
    c = t.read()

separated = c.split("\n")
c = ""
for item in separated:
    c += item
# now c is the code is the code without the language having modified it yet


ops = [   #just shows what characters/strings the program will be looking out for
    "+",
    "-",
    "*",
    "/",
    "%",
    "==",
    "=",
    "!=",
    ">",
    "<",
    "<=",
    ">=",
    "or",
    "and",
    "not",
    ":",
    "?",
    ",",
    "if",
    "else",
    "elif",
    "while"
]


#IMPORTANT NOTe the way tuples and stuff work is that commas are actually operators a,b where they operate on a and b making them a tuple / list !!!! this is cool


opinfo = { #opname:(precedence(higher is better),left associative?
    "+":(0,True)
}



#ternary operator is c?a:b
#tuples are going to be used for functions
    
# I need to separate the read token and then make lists calls and everything be different types of tokens (:
# use shunting yard

def lex(c):
    #Token types are 
    #paren - parenthesis
    #num - any number
    #str - a string
    #op - an operator(not a function created in code)
    #func - a function defined in code
    #bool - a boolean True or False
    #var - a variable
    
    #To do - ternary ops, [] bracket handling (lists and other stuff), comma handling
    lexed = []

    parenc = {
    "{":0,
    "}":0,
    "(":0,
    ")":0,
    "[":0,
    "]":0
    }
    replacenextclosebracket = False #used because my code basically converts var[3] to var.(3) while keeping lists in their original form
    openedparen = ""
    l = 0  # letter

    while l<len(c):
        previousl = l# used to determine invalid syntax
        while c[l] == " ":
            l += 1
        if c[l] in "{}[]()":
            if c[l] in "{[(":
                openedparen = c[l]
            parenc[c[l]] += 1
            if c[l] == "[" and (len(lexed)>0 and lexed[len(lexed)-1][0] == "var"):
               lexed.append(["op","."])
               lexed.append(["paren","("])
               openedparen = "("
               replacenextclosebracket = True
               l += 1
               continue
            if c[l] == "]" and replacenextclosebracket == True:
               lexed.append(["paren",")"])
               replacenextclosebracket = False
               l += 1
               continue
            lexed.append(["paren", c[l]])
            l += 1
        elif c[l].isnumeric():
            t = ""
            points = 0
            while c[l].isnumeric() or c[l] == ".":
                if c[l] == ".":
                    if points > 0:
                        break
                    points += 1
                t += c[l]
                l += 1
                if l >= len(c):
                    break
            lexed.append(["num", float(t)])
        elif c[l] == '"' or c[l] == "'":
            q = c[l]
            t = ""
            l += 1
            while c[l] != q:
                if c[l] == "\\":
                    l += 1
                t += c[l]
                l += 1
            lexed.append(["str", t])
            l += 1
        elif c[l].isalpha():  # is a function or variable
            t = ""
            while c[l].isnumeric() == True or c[l].isalpha() == True:
                t += c[l]
                l += 1
                if l >= len(c):
                    break

            if t in ops:
                lexed.append(["op", t])
            else:
                if l < len(c) and c[l] == "(":
                    lexed.append(["func", t])
                else:
                    if t == "True" or t == "False":
                        lexed.append(["bool", t])
                    else:
                        lexed.append(["var", t])
        else:  # is an operator
            t = ""

            while t == "" or (t + c[l]) in ops:
                t += c[l]
                l += 1
                if l >= len(c):
                    break
            if t == ",":
                if openedparen == "(" or openedparen == "":
                    t = ".t"
                elif openedparen == "[":
                    t = ".l"
            if t == "-":
                if lexed == [] or (lexed[len(lexed)][0] == "paren" and lexed[len(lexed)][1] in ")]}"):
                    t == "-un" #unary negative symbol
            lexed.append(["op", t])
        if previousl == l:
            print("invalid syntax")
            return None
    
    
    if not (parenc["{"] == parenc["}"] and parenc["["] == parenc["]"] and parenc["("] == parenc[")"]):
        print("unmatched brackets")
        return None
    for item in lexed:
        pass
        # yield item
    return lexed
    



print(lex(c))




#uses the shunting yard algorithm
def compile(t): #returns a list of instructions that the stack machine can run given lexed tokens
    length = len(list(t))
    instructions = []
    opstack = []
    tokcount = 0
    while tokcount<len(t):
        tok = next(t)
        ttype = tok[0]
        
        if ttype == "num" or ttype == "str":
            instructions.append(ttype)
        elif ttype == "paren":
            
        elif ttype == "op":
        
        
        tokcount += 1
       
       
       
       
    