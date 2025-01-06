def check(func):
    def wrapper(a,b):
        if b==0:
            return 'Denominator cannot be zero'
        else:
            return func(a,b)
    return wrapper
@check
def div(a,b):
    return a/b
