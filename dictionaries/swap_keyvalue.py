"""1.	Write a program to invert a dictionary (swap keys and values)."""
dict_1={1:"MY",2:"name",3:"is",4:"Ravikiran"}
dict_2={}
for key in dict_1:
    dict_2[dict_1[key]]=key    
print(dict_2)

##This is just for understanding
dict_1={1:"MY",2:"name",3:"is",4:"Ravikiran"}
dict_2={}
for key in dict_1:
    print(key)          # output 1,2,3,4
    print(dict_1[key])          #output "my"...
    dict_2[dict_1[key]]=key  #dict_1[key] values are swaped as key in dict_2
print(dict_2)


