def myDecorators1(func):
    def wrapper():
        print('Действие до функции')
        func()
        print('Действие после функции')
    return wrapper

@myDecorators1
def startD1():
    print('hello goose')

# startD1()

def myDecorators2(count):
    def decoratorsRepeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decoratorsRepeat

@myDecorators2(count=3)
def startD2(price):
    print(price)

# startD2(5)

from functools import wraps

def myDecorators3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('действие до функции')
        result = func(*args, **kwargs)
        print('действие после функции')
        return result
    return wrapper

@myDecorators3
def startD3():
    """print - hello goose"""
    print('hello goose')

# print(startD3.__name__)
# print(startD3.__doc__)

def myDecorators4(count):
    def myDecorators(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return myDecorators

@myDecorators4(count=3)
def startD4(price):
    print(price)

# startD4({'3': 3, '4': 4})

def checkNumberFunctionRuns(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(func, 'max_count'):
            func.max_count = 0
        if func.max_count >= 2:
            return 'error'
        result = func(*args, **kwargs)
        func.max_count += 1
        return result
    return wrapper

@checkNumberFunctionRuns
def check():
    print('hello goose')

# check()
# check()
# print(check())

def checkNumberFuncRunsParam(max_count):
    def decorators(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not hasattr(func, 'count'):
                func.count = 0
            if func.count >= max_count:
                return 'error'
            result = func(*args, **kwargs)
            func.count += 1
            return result
        return wrapper
    return decorators

@checkNumberFuncRunsParam(max_count=1)
def checkParam(name):
    print(f'hello {name}')

# checkParam('goose')
# checkParam('goose')
# checkParam('goose')
# checkParam('goose')
# checkParam('goose')