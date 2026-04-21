#Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets:
list_comp = [x*x for x in range(5,10)]
print(list_comp)#[25, 36, 49, 64, 81]
#generator expression
gen_exp = (x*x for x in range(5,10))
print(gen_exp)#only memory address dikha gha
print(list(gen_exp))
gen_exp = (x*x for x in range(5,10))
for x in gen_exp:
        print(x)



