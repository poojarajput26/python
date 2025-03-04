def outer_function(msg):
    def inner_function():
        print("Message:", msg)
    return inner_function

closure_func = outer_function("Hello Python")
closure_func()
