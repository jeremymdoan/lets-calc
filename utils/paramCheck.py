def checkMatrixSize(M, l):
    notMxN = False
    for row in M:
        if len(row) < l:
            notMxN = True
            break
    return notMxN


def guassParams(data):
    return (
        data.get('params') == None or 
        data['params'].get('A') == None or 
        len(data['params']['A']) < 2 or 
        checkMatrixSize(data['params']['A'], len(data['params']['A'])) or
        data['params'].get('x') == None or 
        len(data['params']['x']) != len(data['params']['A'])
    )

def aAndBParams(data):
    return (
        data.get('params') == None or 
        data['params'].get('a') == None or 
        data['params'].get('b') == None
    )

def aBandCParams(data):
    return (
        data.get('params') == None or 
        data['params'].get('a') == None or 
        data['params'].get('b') == None or 
        data['params'].get('c') == None
    )