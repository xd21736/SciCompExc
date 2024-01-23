"""Solvers"""
def NextN(x, err, F, Fprime):
    if abs(F(x))<err:
        return (x)
    else:
        print(x)
        return(NextN(x-(F(x)/Fprime(x)),err,F,Fprime))
        