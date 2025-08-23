def foo():
    x=10
    y=3
    bar(y,x,x)
    print(x)
    print(y)

def bar(x,y,z):
    y = y + 4
    z = x + y + z

foo()