def prefix_decorator(prefix,postfix):
    def decorator_func(func):
        def wrap_func(*args,**kwargs):
            print(prefix,'executed before ', func.__name__)
            result = func(*args, **kwargs)
            print(postfix,'This is after executing',func.__name__, '\n')
            return result
        return wrap_func
    return decorator_func


@prefix_decorator('Login: ', 'logout: ')
def need_decorator(name, age):
    print('The name and Age {} {}'.format(name, age))

need_decorator('arash',28)