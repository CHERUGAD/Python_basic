def func1():
    x=10
    def func2():
        return x+1
    return func2()
result=func1
print(result())  # Output: 11