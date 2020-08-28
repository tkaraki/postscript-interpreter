# NAME: Tala Karaki



#--------------------------------------------------------------
#                           PART 1
#--------------------------------------------------------------



#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

def opPop():
    if(len(opstack)>0): 
        return opstack.pop()
    else: 
        print ("Error: pop from empty list.")
   

def opPush(value): 
    if (type (value) is bool) or (type (value) is int) or (type (value) is str) or (type (value) is list) or (type (value) is dict): 
        opstack.append(value)
    else: 
        print("Error : type must be bool, int, string, list, or dictionary.")
    

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list


def dictPop():
    if(len(dictstack)>0):  
        return dictstack.pop()
    else: 
        print ("Error: pop from empty list.")
    

def dictPush(d):
    if (type (d) is dict) : 
        dictstack.append(d)
    else: 
        print("Error : type must be dictionary.")
    

def define(name, value):
    myDict = dictPop()
    if (myDict == None):
        myDict = {}
    if (type (name) is str) :  
        myDict[name] = value
        dictstack.append(myDict)
    else:
        print("Error: dict key must be string")
   

def lookup(name):
    myName = '/' + name
    myOp= reversed(dictstack)
    for dict in myOp:
        if myName in dict :
            return dict[myName]
        else:
            print("Error: value not found.")
               

#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not 

def add():
    if(len(opstack)>1):
        op2 = opPop() 
        op1 = opPop()
        if (type (op1) is int and type (op2) is int) :
            opPush(op2 + op1)
        else:
            print("Error: operand not int")
    else:
        print("Error: add needs 2 operands")


def sub():
    if(len(opstack)>1):
        op2 = opPop() 
        op1 = opPop()
        if (type (op1) is int and type (op2) is int) :
            opPush(op1 - op2)
        else:
            print("Error: operand not int")
    else:
        print("Error: sub needs 2 operands")


def mul():
    if(len(opstack)>1):
        op2 = opPop() 
        op1 = opPop()
        if (type (op1) is int and type (op2) is int) :
            opPush(op2 * op1)
        else:
            print("Error: operand not int")
    else:
        print("Error: mul needs 2 operands")


def eq():
    if(len(opstack)>1):
        op2 = opPop() 
        op1 = opPop()
        if (op2 == op1): 
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error: eq needs 2 operands")


def lt():
    if(len(opstack)>1):
        op2 = opPop() 
        op1 = opPop()
        if (op1 < op2): 
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error: lt needs 2 operands")


def gt():
    if(len(opstack)>1):
        op2 = opPop() 
        op1 = opPop()
        if (op2 > op1): 
            opPush(False)
        else:
            opPush(True)
    else:
        print("Error: gt needs 2 operands")


def psAnd():
    if(len(opstack)>1):
        op2 = opPop() 
        op1 = opPop()
        if (type (op1) is bool and type (op2) is bool) :
            if (op1==True and op2==True): 
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: type must be bool")
    else:
        print("Error: psAnd needs 2 operands")


def psOr():
    if(len(opstack)>1):
        op2 = opPop() 
        op1 = opPop()
        if (type (op1) is bool and type (op2) is bool) :
            if (op1==False and op2==False): 
                opPush(False)
            else:
                opPush(True)
        else:
            print("Error: type must be bool")
    else:
        print("Error: psAnd needs 2 operands")    


def psNot():
    if(len(opstack)>0):
        op1 = opPop()
        if (type (op1) is bool) :
            if (op1 == True): 
                opPush(False)
            elif (op1 == False):
                opPush(True)
        else:
            print("Error: type must be bool")
    else:
        print("Error: stack is empty")    

#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    item = opPop()
    opPush(len(item))

def get():
    index = opPop()
    array = opPop()
    opPush(array[index])

def getinterval():
    count = opPop()
    index = opPop()
    array = opPop()
    opPush(array[index:(index+count)])

def put():
    value = opPop()
    index = opPop()
    array = opPop()
    array[index] = (value)
    return array

def putinterval():
    array2 = opPop()
    index = opPop()
    array1 = opPop()
    for i in range(len(array2)): 
        array1[i + index]= array2[i]
    opPop()
    opPush(array1)

#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark

def dup():
    if(len(opstack)>0):
        dup = opPop()
        opPush(dup)
        opPush(dup)
    else:
        print("Error: stack is empty")

def copy():
    count = opPop()
    mylist = count*[None]
    for i in range (count): 
        mylist[i] = opPop()
    mylist.reverse()
    for elem in mylist:
        opPush(elem)
    for elem in mylist: 
        opPush(elem)

def count():
    opPush(len(opstack))

def pop():
    opPop()

def clear():
    while len(opstack) != 0:
        opPop()

def exch():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        opPush(op2)
        opPush(op1)
    else:
        return "Error: exch needs 2 operands."


def mark():
    opPush('-mark-')


def cleartomark():
    if opPop() == '-mark':
        return
    else:
        while(len(opstack) != 0) :
            if opPop() == '-mark-':
                return


def counttomark():
    index = -1
    count = 0
    while ( opstack[index] != ('-mark-') ):
        count = count + 1
        index = index - 1
    opPush(count)


def stack():
    if (len(opstack)>0):
        mylist = reversed(opstack)
        for i in mylist:
            print ('\n' + mylist[i])
    else:
        print("Error: empty stack.")

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    if len(opstack)>0:
        size = opPop()
        if (isinstance(size,int)): 
            mydict = {}
            opPush(mydict)
        else:
            print("Error: set dict size with int")
    else:
        print("Error: empty stack.")


def begin():
    if len(opstack)>0:
        mydict = opPop()
        dictPush(mydict)
    else:
        print("Error: empty stack.")


def end():
    if len(opstack)>0:
        dictPop()
    else:
        print("Error: empty stack.")


def psDef():
    if len(opstack)>1:
        value = opPop()
        name = opPop()
        if isinstance(name,str):
            define(name,value)
        else:
            print("Error: dict key must be string")
    else:
        print("Error: def needs 2 operands")
    




#--------------------------------------------------------------
#                           PART 2
#--------------------------------------------------------------

import re
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
 
#---------------------------------------------------------------
# Stack operators: psIf, psIfElse, psForall, psRepeat, forLoop, forAll
#---------------------------------------------------------------

def psIf():
    func = opPop()
    val = opPop()
    if (type (val) is bool):
        if (val==True):
            interpretSPS(func)

def psIfElse():
    func2 = opPop()
    func1 = opPop()
    val = opPop()
    if (type (val) is bool):
        if (val==True):
            interpretSPS(func1)
        else:
            interpretSPS(func2)

def psForall():
    func = opPop()
    array = opPop()
    for item in array:
        opPush(item)
        interpretSPS(func)

def psRepeat():
    func = opPop()
    n = opPop()
    count=0;
    if (type (n) is int):
        while count!=n:
            interpretSPS(func)
            count+=1

def forLoop():
    func = opPop() 
    l = opPop() 
    k = opPop() 
    j = opPop()
    for i in range(j, k, l):
        opPush(i)
        interpretSPS(func)

def forAll():
    func = opPop() 
    array = opPop() 
    for i in array:
        opPush(i)
        interpretSPS(func)


#--------------------------------------------------------------------------------------------------------------
# Interpreter operators: groupMatch, parseMatch, interpretSPS, interpreter, clearStack, isInt, isBool, toBool
#--------------------------------------------------------------------------------------------------------------
    
def isBool(s):
    if s in ['true', 'false']:
        return True
    else:
        return False


def toBool(s):
    if s=='true':
        return True
    elif s=='false':
        return False


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            res.append(groupMatch(it))
        else:
            if isBool(c):
                c = toBool(c)
            elif isInt(c):
                c = int(c)
            elif c[0]=='[':
                array = []
                stringArray = c[1:-1].split(' ')
                for item in stringArray:
                    if isBool(item):
                        array.append(toBool(item))
                    elif isInt(item):
                        array.append(int(item))
                    else: 
                        array.append(item)
                c = array
            res.append(c)
    return False


def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            if isBool(c):
                c = toBool(c)
            elif isInt(c):
                c = int(c)
            elif c[0]=='[':
                array = []
                stringArray = c[1:-1].split(' ')
                for item in stringArray:
                    if isBool(item):
                        array.append(toBool(item))
                    elif isInt(item):
                        array.append(int(item))
                    else: 
                        array.append(item)
                c = array
            res.append(c)
    return {'codearray':res}


def interpretSPS(code):
    for item in code['codearray']:
        if isinstance(item, bool):
            opPush(item)   
        elif isinstance(item, int):
            opPush(item)
        elif isinstance(item, dict):
            opPush(item) 
        elif isinstance(item, list):
            opPush('-mark-')
            interpretSPS({'codearray':item})
            innerlist= opPop()
            mylist  = []
            while innerlist!='-mark-':
                mylist.append(innerlist)
                innerlist = opPop()
            mylist.reverse()
            opPush(mylist) 
        elif isinstance(item, str):
            if item[0] == '/':
                opPush(item)
            elif item=='and': 
                psAnd()
            elif item=='or':
                psOr()
            elif item=='not': 
                psNot()
            elif item=='add':
                add()
            elif item=='sub':
                sub()
            elif item=='mul':
                mul()
            elif item=='eq':
                eq()
            elif item=='lt':
                lt()
            elif item=='gt':
                gt()
            elif item=='put':
                put()
            elif item=='putinterval':
                putinterval()
            elif item=='get':
                get()
            elif item=='getinterval':
                getinterval()
            elif item=='length':
                length()
            elif item=='if':
                psIf()
            elif item=='ifelse':
                psIfElse()
            elif item=='repeat':
                psRepeat()
            elif item=='forall':
                psForall()
            elif item=='dict':
                psDict()
            elif item=='begin':
                begin()
            elif item=='end':
                end()
            elif item=='def':
                psDef()
            elif item=='copy':
                copy()
            elif item=='clear':
                clear()
            elif item=='stack':
                stack()
            elif item=='dup':
                dup()
            elif item=='exch':
                exch()
            elif item=='pop':
                pop()
            elif item=='count':
                count()
            elif item=='mark':
                mark()
            elif item=='counttomark':
                counttomark()
            elif item=='cleartomark':
                cleartomark()
            else:
                dictVal = lookup(item)
                if isinstance(dictVal, dict):
                    interpretSPS(dictVal)
                else:
                    opPush(dictVal)
        else:
            opPush(item)


def interpreter(s):
    interpretSPS(parse(tokenize(s)))


def clearStacks():
    opstack[:] = []
    dictstack[:] = []

testinput2 = """
            /x 1 def
            /y 2 def
            1 dict begin
            /x 10 def
            1 dict begin /y 3 def x y end
            /y 20 def
            x y
            end
            x y
        """

interpreter(testinput2)