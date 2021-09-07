# FUNCTIONS
def my_func(param1='default'):
    '''
    this is a doc string
    '''
    print('first {}'.format(param1))

my_func()

def hello():
    print('hello')

hello()

def bye():
    return 'bye'

result = bye()
print(result)

def addNum(num1, num2):
    return num1 + num2

total = addNum(2,4)
print(total)
print(type(total))

def addNum(num1, num2):
    return num1 + num2

tot = addNum("2","4")
print(tot)
print(type(tot))

def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return 'I need integers'

test = addNum("2",4)
print(test)

# Lambda expression
# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(list(evens))

# Lambda
even = filter(lambda num: num%2 == 0, mylist)
print(list(even))

# other
tweet = 'go sports! #sports'
text = tweet.split('#')[1]
print(text)

print('x' in [1,2,3])