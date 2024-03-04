#functions - 2/3
# Topic 1: Global Variables
#- Defined outside any functions
#- has a global scope, starting fomr the pplace it is defined

def foo(x, y, z):
    x = 1
    y = 100
    z = 50.50
    if x > y:
        foo = "error"
    else:
        avg = (x + y)/2
        if avg > z:
            foo = "good"
        elif avg == z:
            foo = "ok"
        elif avg < z:
            foo = "bad"

# Examples
foo(1, 100, 55.0) 
foo(3, 33, 35.47)   
foo(48, 12, 56.78)   
foo(12, 12, 12.0)
foo(55, 88, 134.56)
foo(-32, -16, -45.67)
foo(55, 88)
foo(76, 34)
foo(123)
foo()    








# Topic 2: Random Numbers
# Topic 3: Returning Values
