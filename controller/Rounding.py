def rounding(n):
    M,N=divmod(n,0.5)

    if N>=0.25:
        return (M+1)*0.5
    elif N<0.25:
        return M*0.5
