'''
LEGB

Local (L): names assigned in any way within a function (def or lambda) and not declared global in that function
Enclosing Function locals (EFLs): name in the local scope of any and all enclosing functions (def or lambda) from inner to outer
Global (G): names assigned at the top level of a module file, or declared global in a def within the file
Built-in (B): names preasigned in the built-in names module: open, range, SyntaxError

'''

x = 25

def func():
    x = 50
    return x

print(func())   # 50
print(x)        # 25

# Local
lambda k: k**2

# Enclosing Function locals
name = 'this is a global name'

def greet():
    name = 'sammy'

    def hello():
        print('hello ' + name)

    hello()

greet()
print(name) # 'this is a global name'

# local variable names
d = 50 

def fun(d):
    print('d is:', d)
    d = 1000
    print('local d changed to:', d)

fun(d)
print(d)

def glo():
    global d # changes global variable
    d = 150

print(d) 
glo()
print(d)