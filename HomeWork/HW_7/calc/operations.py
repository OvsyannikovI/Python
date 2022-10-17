global x
global y

actions = {
    "^": lambda x,y: str(float(x)**float(y)),
    "*": lambda x,y: str(float(x)*float(y)),
    "/": lambda x,y: str(float(x)/float(y)),
    "+": lambda x,y: str(float(x)+float(y)),
    "-": lambda x,y: str(float(x)-float(y)),
}

dict_act = {
    "1": "^",
    "2": "*",
    "3": "/",
    "4": "+",
    "5": "-",
}