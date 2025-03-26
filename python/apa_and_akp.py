def my_func(*args,**kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print( f"My details is {key} :{value}")
my_func(10,20,30,40,)
my_func(name =':ravi',middle_name="p",last_name ="cherugad")