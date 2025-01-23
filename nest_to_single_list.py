nested_list = [1, [2, [3, 4], 5], [6, 7], 8]
new_list=[]
stack=nested_list.copy()
while stack:
    element = stack.pop()
    if isinstance(element, list):
        stack=element+stack
    else:
        new_list.append(element)
print(new_list)