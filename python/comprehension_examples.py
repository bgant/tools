# Source: YouTube "25 nooby Python habits you need to ditch" by mCoding Nov 15, 2021

dict_comp = {i: i*i for i in range(10)}
list_comp = [x*x for x in range(10)]
set_comp  = {i%3 for i in range(10)}
gen_comp  = (2*x+5 for x in range(10))

print(dict_comp)
print(list_comp)
print(set_comp)
print(gen_comp)
