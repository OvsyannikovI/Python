global x
global y

actions_complex = {
    "^": lambda x,y: str(complex(x)**complex(y)),
    "*": lambda x,y: str(complex(x)*complex(y)),
    "/": lambda x,y: str(complex(x)/complex(y)),
    "+": lambda x,y: str(complex(x)+complex(y)),
    "-": lambda x,y: str(complex(x)-complex(y)),
}

actions_float = {
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