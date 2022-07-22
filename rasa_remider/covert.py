import json
from turtle import xcor
from uit_member import a
s = []
for x in a:
    value = x.values()
    values = list(value)
    s+=values
with open("test.txt",'w',encoding = 'utf-8') as f:
    for i in s:
        if i !="":
            f.write(i+"\n")
