# Define a decorator
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

# Apply decorator to a function
@my_decorator
def say_hello():
    print("Hello!")
say_hello()

