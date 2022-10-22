import operations as op


def view_data(data):
    print(f'result = {data}')

def get_value():
    return input('Enter number = ')
    
def isNumeric(s):
    try:
        complex(s)
        return True
    except ValueError:
        return False